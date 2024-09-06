from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('chef', 'Chef'),
        ('admin', 'Admin'),
    ]
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/')
    user_type = models.CharField(max_length=5, choices=USER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    def register(self):
        pass

    def login(self):
        pass

    def updateProfile(self):
        pass

    def makeBooking(self):
        pass

    def leaveRatingReview(self):
        pass

    def makePayment(self):
        pass
