from django import forms
from .models import Dropdown

class DropdownForm(forms.ModelForm):
    dropdown = forms.MultipleChoiceField(choices=(("Text", "Text"),("Image", "Image"),("Audio", "Audio")),widget=forms.SelectMultiple(attrs={
                                "class": "form-control",
                                "multiple":"true",
                                "multiselect-search": "true",
                                "multiselect-select-all": "true"
                            }
                        ),required=False
                    )
    class Meta:
        model = Dropdown
        fields = ["dropdown","textarea","image","audio"]
        widgets={
            "textarea":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.Textarea(attrs={"class":"form-control"}),
            "audio":forms.Textarea(attrs={"class":"form-control"}),
            
        }