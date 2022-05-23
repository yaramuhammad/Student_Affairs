from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class NewUserForm(UserCreationForm):
    forms.ModelForm.error_css_class = 'error-field'
    email = forms.EmailField(label='',required=True, widget=forms.EmailInput(attrs={
        "class": "bar2",
        "id": "email",
        "placeholder":"Email",
    }))
    username = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={
        "class": "bar2",
        "id": "fname",
        "placeholder": "Username",
    }))
    password1 = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={
        "class": "bar2",
        "id": "pass",
        "placeholder": "Password",
    }))
    password2 = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={
        "class": "bar2",
        "id": "pass-confirm",
        "placeholder": "Confirm Password",
    }))
    # <input class="bar2" type="Password" id="pass-confirm" placeholder="Confirm Password" required><br>#}
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = re.compile("^[A-Za-z]\w*@[A-Za-z]\w*.[A-Za-z]{2,3}$")
        if not email_regex.search(email):
            raise forms.ValidationError("Invalid Email")
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise forms.ValidationError("Invalid Email")
        return username

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

