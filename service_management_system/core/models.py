# from django.db import models
# from django.contrib.auth.models import User
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add other profile fields
#
# class Service(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     # Add other fields for service details
#
# class ServiceRequest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     description = models.TextField()
#     # Add other fields for request details
#
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#
#     class UserProfile(models.Model):
#         user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#         # Add other profile fields
#
#         class Meta:
#             app_label = 'core'
#
#     # Add other fields like date, status, etc.
#
# # Define other models like Feedback, KnowledgeBase, etc.

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other profile fields

    class Meta:
        app_label = 'core'

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields for service details

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    # Add other fields for request details

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    # Add other fields like date, status, etc.

    class Meta:
        app_label = 'core'

# Define other models like Feedback, KnowledgeBase, etc.
