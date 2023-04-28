from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment, Feedback
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    name = forms.TextInput()
    phone_number = forms.TextInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AppointmentCreateForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'start_time']

class FeedbackCreateForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['appointment', 'feedback']

