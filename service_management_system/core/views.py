from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import Notification

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('service_catalog')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'notifications.html', {'notifications': notifications})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def service_catalog(request):
    # Fetch and pass service catalog data to the template
    service_list = []  # Placeholder for service catalog data, replace with your actual data
    return render(request, 'service_catalog.html', {'service_list': service_list})

from django.shortcuts import render

def services(request):
    # Add logic to fetch and pass service data to the template if needed
    return render(request, 'service.html')

def contact(request):
    # Add logic to handle contact form submission if needed
    return render(request, 'contact.html')

def bookingpage(request):
    # Add logic to handle contact form submission if needed
    return render(request, 'bookingpage.html')

def home(request):
    # Add logic to handle contact form submission if needed
    return render(request, 'home.html')

def home(request):
    # Add logic to handle contact form submission if needed
    return render(request, 'home.html')

def About_Us(request):
    # Add logic to handle contact form submission if needed
    return render(request, 'About_Us.html')

def contact(request):
    # Add logic to handle contact form submission if needed
    return render(request, 'Contact.html')

def Sign_Out(request):
    # Add logic to handle contact form submission if needed
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import ServiceRequest

def booked_services(request):
    # Retrieve all booked services from the database
    booked_services = ServiceRequest.objects.all()
    return render(request, 'booked_services.html', {'booked_services': booked_services})

# views.py
from django.shortcuts import render
from .models import ServiceRequest

def booked_services(request):
    booked_services = ServiceRequest.objects.all()
    return render(request, 'booked_services.html', {'booked_services': booked_services})

# views.py
from django.shortcuts import render
from .models import ServiceRequest

def booked_services(request):
    booked_services = ServiceRequest.objects.all()
    return render(request, 'booked_services.html', {'booked_services': booked_services})






