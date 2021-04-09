from django import forms

# FORM FOR LOGIN
class LoginForm(forms.Form):
    email = forms.CharField(label="email",required = True)
    password= forms.CharField(label="password",required = True)
