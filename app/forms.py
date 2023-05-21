from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["firstname","lastname","email","phone_number"]
        labels={
            "firstname":"First name",
            "lastname":"Last name",
            "email":"Email",
            "phone_number":"Phone number"
        }
        widgets={
            "firstname":forms.TextInput(attrs={"class":"form-control"}),
            "lastname":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control"}),
        }

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')  # Remove the 'password' field from the form

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active']
        labels = {
            'email': 'Email'
        }

class AdminEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')  # Remove the 'password' field from the form

    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'email': 'Email'
        }