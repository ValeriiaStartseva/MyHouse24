from django.views.generic import View
from django.shortcuts import render, redirect
from src.users.forms.create_staff_user_form import CreateStaffUserForm
from src.users.models import User
from src.roles.models import RolePermission
from src.users.tasks import send_email_task


class CreateStaffUserView(View):
    template_name = "users/admin/create_staff_user.html"
    form_class = CreateStaffUserForm

    def get(self, request):
        print("Entering GET method of CreateStaffUserView")
        form = self.form_class()
        roles = RolePermission.objects.all()
        print(f"Roles fetched: {[role.name for role in roles]}")
        status_choices = User.STATUS_CHOICES
        print(f"Status choices: {status_choices}")
        return render(
            request,
            self.template_name,
            {"form": form, "roles": roles, "status_choices": status_choices},
        )

    def post(self, request):
        print("Entering POST method of CreateStaffUserView")
        form = self.form_class(request.POST)
        if form.is_valid():
            print("Form is valid. Proceeding with user creation.")
            user = form.save(commit=False)
            password = form.cleaned_data["password1"]
            print(f"Password from form: {password}")
            user.set_password(password)
            user.is_staff = True

            # Зберігаємо користувача для отримання ID
            user.save()

            # Зберігаємо вибрану роль
            role = form.cleaned_data["role"]
            user.role = role
            user.save()
            print(f"User created with email: {user.email} and role: {user.role.name}")

            # Підготовка даних для листа
            subject = "Ваш обліковий запис адміністратора створено"
            context = {
                "admin_user_name": user.name,
                "roles": user.role.name,
                "password": password,
            }

            # Викликаємо завдання Celery для асинхронної відправки листа
            try:
                send_email_task.delay(
                    subject, "emails_template/account_create.html", context, user.email
                )
                print(f"Email sent to {user.email} with subject '{subject}'")
            except Exception as e:
                print(f"Failed to send email: {e}")

            return redirect("users-staff")
        else:
            print("Form is invalid. Errors:", form.errors)
            roles = RolePermission.objects.all()
            status_choices = User.STATUS_CHOICES
            return render(
                request,
                self.template_name,
                {"form": form, "roles": roles, "status_choices": status_choices},
            )
