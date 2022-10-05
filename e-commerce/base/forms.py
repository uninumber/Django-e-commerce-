from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'password11',
            'id':'password11',
            'type':'text',
            'class':'form-input',
            'placeholder': 'username',
            'maxlength':'16',
            })

    
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-input',
            'placeholder': 'example@gmail.com',
            'maxlength':'16',
            'minlength':'6',
            })

        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'text',
            'class':'form-input',
            'placeholder': '********',
            'maxlength':'16',
            'minlength':'6',
            })


        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password2',
            'class':'form-input',
            'placeholder': '********',
            'maxlength':'16',
            'minlength':'6',
            })



   






    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       

        def save(self, commit=True):

            user = super(RegistrationForm, self).save(commit=False)
 

            if commit:
                user.save()

            return user

