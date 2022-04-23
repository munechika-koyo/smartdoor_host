from django.contrib.auth.forms import AuthenticationForm
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Key


class LoginForm(AuthenticationForm):
    """Custom Login Form
    add some class and placeholder values into widget attributes
    """

    def __init__(self, request=None, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label


class KeyModelForm(BSModalModelForm):
    class Meta:
        model = Key
        fields = (
            "name",
            "device",
            "idm",
            "allow_423",
            "allow_475",
        )
        widgets = {
            "allow_423": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "allow_475": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class KeyRegisterForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = (
            "name",
            "device",
            "idm",
            "allow_423",
            "allow_475",
        )
        widgets = {
            "allow_423": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "allow_475": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
