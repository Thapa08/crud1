from django import forms
from .models import Member

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
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control"}),
        }