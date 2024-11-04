from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from src.users.models import User


@shared_task
def send_confirmation_email(user_id, domain):
    try:
        user = User.objects.get(pk=user_id)
        mail_subject = "Активуйте свій обліковий запис"
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        message = render_to_string(
            "users/email_confirmation.html",
            {
                "user": user,
                "domain": domain,
                "uid": uid,
                "token": token,
            },
        )

        send_mail(
            mail_subject,
            message,
            "no-reply@mydomain.com",
            [user.email],
            fail_silently=False,
        )
    except User.DoesNotExist:
        pass  # Обробка випадку, коли користувача немає
