from django import forms
from .models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["title","starting_date","ending_date","description"]


class ContactUsForm(forms.Form):
    name = forms.TextInput()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)