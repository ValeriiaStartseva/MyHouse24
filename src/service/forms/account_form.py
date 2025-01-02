from django import forms

from src.service.models import Account


class AccountForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        required=True,
        label="Назва",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    type = forms.ChoiceField(
        choices=Account.TYPE_CHOICES,
        required=True,
        label="Прихід/Розхід",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Account
        fields = ["name", "type"]
