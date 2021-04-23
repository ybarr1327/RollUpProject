from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from.models import Participants

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(label='Enter Email')
    first_name = forms.CharField(label = 'First Name', min_length=4, max_length=150)
    last_name = forms.CharField(label = 'Last Name', min_length=4, max_length=150)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


    def save(self, commit=True):
        
        user = super(CustomUserCreationForm,self).save(commit=False)
        
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()

        return user

    

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        return last_name

class participantCreationForm():

    class Meta:
        model = Participants
        fields = ['class_id','name','email']

    def save(self, commit=True):
        participant = super(participantCreationForm,self).save(commit=False)
        form.instance.email = self.request.user['email']
        form.instance.name = self.request.user['first_name']
        
        if commit:
            participant.save()

        return participant