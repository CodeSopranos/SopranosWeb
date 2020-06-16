from django import forms


# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=150)
#     password = forms.CharField(label='Password', max_length=1024, widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='Email', max_length=256)
    password = forms.CharField(label='Password', max_length=1024, min_length=3, widget=forms.PasswordInput)
    password_again = forms.CharField(label='Password, again', max_length=1024, min_length=3, widget=forms.PasswordInput)
