from django import forms
from .models import Notes
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['heading','content']
        widgets={
            "heading":forms.TextInput(attrs={"class":"form-control","id":"headid"}),
            "content":forms.Textarea(attrs={"class":"form-control","id":"contentid","rows":"3"}),

        }