from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.views import View
from django.shortcuts import redirect
from django.conf import settings
from src.users.models import User


class ActivateAccountByEmailView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.status = "new"  # status also new, because admin need acsept user
            user.email_verified = True  # Поле email_verified стає True
            user.save()

            # Виконуємо авторизацію користувача після активації
            user.backend = settings.AUTHENTICATION_BACKENDS[0]  # Вказуємо backend
            login(request, user, backend=user.backend)
            return redirect(
                "login"
            )  # поки логін, потім змінити або на сводку, або на статистику взалежності від ролі
        else:
            return redirect(
                "activation_invalid"
            )  # Якщо токен недійсний або користувача не знайдено
