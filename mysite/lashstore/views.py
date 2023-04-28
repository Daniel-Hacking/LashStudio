from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Service, Appointment, Feedback
from .forms import RegistrationForm, AppointmentCreateForm, FeedbackCreateForm
from django.contrib import messages
from datetime import datetime

# Create your views here.


def home(request):
    services = Service.objects.all()
    return render(request, 'lashstore/home.html', {'services': services})

def service_detail(request, service_id):
    if request.method == 'POST':
        return redirect(reverse(appointment_create, args={'storyid':service_id}))
    else:
        service = get_object_or_404(Service, pk=service_id)
        return render(request, 'lashstore/service_detail.html', {'service': service})

def appointment_create(request):
    form = AppointmentCreateForm(request.POST or None)

    if form.is_valid():
        appointment = form.save()
        # Redirect the user to the appointment detail page
        return HttpResponseRedirect('appointments/appointment_detail/{}'.format(appointment.id))
    else:
        return redirect('home')

def appointment_list(request):
    if request.user.is_authenticated:
        user = request.user
        appointments = Appointment.objects.filter(user=user)
        return render(request, 'appointments/appointment_list.html', {'appointment': appointments})
    else:
        return redirect('home')
    
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

def appointment_cancel(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return HttpResponseRedirect('home')

def feedback_create(request, appointment_id):
    if request.method == 'POST':
        # Get the posted data
        feedback = request.POST['feedback']

        # Create the feedback
        feedback = Feedback(
            appointment_id=appointment_id,
            feedback=feedback,
        )
        feedback.save()

        # Redirect the user to the appointment detail page
        return HttpResponseRedirect('appointments/appointment_detail/{}'.format(appointment_id))
    else:
        # Get the appointment detail
        appointment = get_object_or_404(Appointment, pk=appointment_id)
        return render(request, 'lashstore/feedback_create.html', {'appointment': appointment})
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            messages.success(request, f'Welcome {username}! Your account has been created.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})
