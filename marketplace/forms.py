from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SasviewModel
from .models import ModelFile

class SasviewModelForm(ModelForm):
    class Meta:
        model = SasviewModel
        fields = ("name", "description")
        help_texts = {
            'description': ("LaTeX formatting is supported. Use $...$ to"
                " denote inline maths, and $$...$$ or \\[...\\] to denote"
                " displayed maths.")
        }

class ModelFileForm(ModelForm):
    class Meta:
        model = ModelFile
        fields = ("model_file",)
        labels = { "model_file": "Upload a model file:" }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    email.help_text = "Required."
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
