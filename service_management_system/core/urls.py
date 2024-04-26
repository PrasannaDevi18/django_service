
from django.urls import path
from . import views
from .views import booked_services

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('submit-service-request/', views.submit_service_request, name='submit_service_request'),
    path('notifications/', views.notifications, name='notifications'),
    path('service-catalog/', views.service_catalog, name='service_catalog'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('login/service.html', views.services , name='service'),
    # path('login/home.html', views.bookingpage , name='bookingpage'),
path('login/home.html', views.home , name='home'),

    path('login/booking_page.html', views.bookingpage , name='bookingpage'),

    path('login/home.html', views.home, name='home'),
     path('login/About_Us.html', views.About_Us, name='About Us'),
    path('login/contact.html', views.contact, name='Contact Us'),
     path('login/Sign_Out.html', views.Sign_Out, name='Sign Out'),
    path('booked-services/', booked_services, name='booked_services'),
    # Other URL patterns

    path('booked-services/', booked_services, name='booked_services'),  # URL pattern for booked services
    path('booked-services/', views.booked_services, name='booked_services'),
    # Add other URL patterns as needed
]



    # path('login/Aboutus.html', views.Aboutus, name='About Us'),

# <li><a href="home.html">Home</a></li>
#             <li><a href="About_Us.html">About Us</a></li>
#             <li><a href="contact.html">Contact Us</a></li>
#             <li><a href="home.html">Sign Out</a></li>


    # Add more URL patterns for other views as needed


