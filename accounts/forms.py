from django import forms
# for password validation
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails  

class SignupForm(UserCreationForm):
    class Meta:
        model = UserDetails
        fields = [
            'username', 'email', 'first_name', 'last_name', 'profile_pic',
            'role', 'address_line1', 'city', 'state', 'pincode',
        ]
    # for checking the availability of username
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if UserDetails.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

