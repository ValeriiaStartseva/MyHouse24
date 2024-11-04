from django.urls import path, include
from .views import CustomSignupView, CustomLoginView

urlpatterns = [
    path("accounts/signup/", CustomSignupView.as_view(), name="register"),
    path("accounts/login/", CustomLoginView.as_view(), name="account_login"),
    path("accounts/", include("allauth.urls")),
]
