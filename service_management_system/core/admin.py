from django.contrib import admin
from .models import UserProfile, Service, ServiceRequest, Notification

admin.site.register(UserProfile)
admin.site.register(Service)
admin.site.register(ServiceRequest)
admin.site.register(Notification)
