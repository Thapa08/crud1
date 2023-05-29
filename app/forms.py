from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class MemberForm(forms.ModelForm):
    # name = forms.CharField(error_messages={'required':'Enter your name'})      
    user = forms.ModelChoiceField(queryset=User.objects.all())
    def __init__(self,user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user'].queryset=User.objects.filter(id=user.id)
        self.fields['user'].widget.attrs.update({'class':'form-control'})

    def clean(self):
        firstname = self.cleaned_data.get('firstname',None)
        data=Member.objects.filter(firstname__iexact=firstname)
        if data.exists():
            self.add_error('firstname','Firstname already exists')
    


    class Meta:
        model = Member
        fields = ["user","firstname","lastname","email","phone_number"]
        widgets={
            "firstname":forms.TextInput(attrs={"class":"form-control"}),
            "lastname":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control"}),
        }

class SignUpForm(UserCreationForm):
    error_css_class = 'error'
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        uname = self.cleaned_data.get('username',None)
        data = User.objects.filter(username__iexact=uname)
        if data.exists():
            raise forms.ValidationError("Username already exists")
        return uname
    
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

