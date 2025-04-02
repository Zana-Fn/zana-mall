from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile

#Edit User Section 
class SignUpForm(UserCreationForm):
    first_name=forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your first name'})
    )
    last_name=forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your last name'})
    )
    email=forms.EmailField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your Email'})
    )
    username=forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your username'})
    )

    password1=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-container',
                'name':'password',
                'type':'password',
                'placeholder':'password: more than 8 char'
             
            }
        )
    )
    password2=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-container',
                'name':'password',
                'type':'password',
                'placeholder':'enter your password again'             
            }
        )
    )
    class Meta:
        model=User
        fields={'first_name','last_name','email','username','password1','password2'}

class UpdateUserForm(UserChangeForm):
    password=None 
    first_name=forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your first name'}),
        required=False
    )
    last_name=forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your last name'}),
        required=False
    )
    email=forms.EmailField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your Email'}),
        required=False
    )
    username=forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Enter your username'}),
        required=False
    )

    class Meta:
        model=User
        fields={'first_name','last_name','email','username'}

class UpdatePasswordForm(SetPasswordForm):
    new_password1=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-container',
                'name':'password',
                'type':'password',
                'placeholder':'password: more than 8 char'
             
            }
        )
    )
    new_password2=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-container',
                'name':'password',
                'type':'password',
                'placeholder':'enter your password again'             
            }
        )
    )
    class Meta:
        model=User
        fields={'new_password1','new_password2'}

#Edit Profile Section 
class UpdateUserInfo(forms.ModelForm):
    phone=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Phone Number:'}),
        required=False
    )
    address1=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Address:'}),
        required=False
    )
    address2=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Address again:'}),
        required=False
    )
    city=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'City:'}),
        required=False
    )

    class Meta:
        model=Profile
        fields=['phone','address1','address2','city']

class UpdateUserInfoRequired(forms.ModelForm):
    phone=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Phone Number:'}),
        required=True
    )
    address1=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Address:'}),
        required=True
    )
    address2=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'Address again:'}),
        required=False
    )
    city=forms.CharField(max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-container', 'placeholder':'City:'}),
        required=True
    )

    class Meta:
        model=Profile
        fields=['phone','address1','address2','city']