from django import forms
from django.core.exceptions import ValidationError

from accounts.models import UserProfile, Experience

def password_len_validator(text):
    if len(text)<8:
        raise  ValidationError('passowrd must be at least 8 character')
class UserCreationForm(forms.Form):
    name=forms.CharField(max_length=100
                         ,help_text='username must be a string'
                         )
    email=forms.EmailField()
    password1=forms.CharField(max_length=200,
                              widget=forms.PasswordInput(),
                              validators=[password_len_validator])
    password2=forms.CharField(max_length=200,
                              widget=forms.PasswordInput(),
                              validators=[password_len_validator])
    # def clean(self):
    #     cleaned_data=super().clean()
    #     password1=cleaned_data.get('password1')
    #     password2=cleaned_data.get('password2')
    #     if password1 != password2:
    #         raise ValidationError('passwords must match')
    #     return  cleaned_data
class UserProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['job_title','bio','picture']
        # exclude = ['user','slug']

class ExperiencecreationForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['userprofile']
