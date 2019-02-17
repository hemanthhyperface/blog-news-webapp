

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import UserInfo


# class CustomUserCreationForm(forms.Form):
#     username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
#     # fullname = forms.CharField(label='enter full name',max_length=50)
#     email = forms.EmailField(label='Enter email')

#     password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


class CustomUserCreationForm(ModelForm):
    fullname = forms.CharField(required=True)
    class Meta:

        model = User
        fields = ['fullname', 'username', 'email','password']
        widgets = {
            'password1': forms.PasswordInput,
            'password2': forms.PasswordInput,
        }

        def save(self, commit=True):
            user = super(CustomUserCreationForm, self).save(commit=False)
            user.fullname = self.cleaned_data["fullname"]
            if commit:
                user.save()
            return user


#     # def clean_username(self):
#     #     username = self.cleaned_data['username']
#     #     if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
#     #         raise forms.ValidationError(u'username "%s" is already in use.' % username)
#     #     return username
        
#         # if r.count():
#         #     raise ValidationError('name exist')
#         # return data
        
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Password don't match")

#         return password2

    
