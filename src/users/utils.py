import secrets
import string

import requests
from allauth.account.models import EmailAddress
from django.conf import settings

from .tasks import send_email_task


def verify_recaptcha(recaptcha_response):
    data = {"secret": settings.RECAPTCHA_PRIVATE_KEY, "response": recaptcha_response}
    try:
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
        result = r.json()

        return result.get("success", False)

    except requests.exceptions.RequestException:
        return False


def is_email_verified(user):
    return EmailAddress.objects.filter(user=user, verified=True).exists()


def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password


def send_admin_account_email(self, admin_user, password):
    subject = "Ваш обліковий запис адміністратора створено"
    roles = ", ".join([role.name for role in admin_user.role.all()])
    context = {
        "admin_user": admin_user,
        "roles": roles,
        "password": password,
    }

    # Викликаємо асинхронне завдання
    send_email_task.delay(
        subject, "emails/account_created_email.html", context, admin_user.email
    )
