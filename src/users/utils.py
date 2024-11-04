import requests
from django.conf import settings
from allauth.account.models import EmailAddress


def verify_recaptcha(recaptcha_response):
    data = {"secret": settings.RECAPTCHA_PRIVATE_KEY, "response": recaptcha_response}
    try:
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
        result = r.json()

        # Додатковий відладочний друк для помилок reCAPTCHA
        if not result.get("success", False):
            print("reCAPTCHA verification failed:", result)

        return result.get("success", False)

    except requests.exceptions.RequestException:
        # Повертає False у випадку помилок
        return False


def is_email_verified(user):
    return EmailAddress.objects.filter(user=user, verified=True).exists()
