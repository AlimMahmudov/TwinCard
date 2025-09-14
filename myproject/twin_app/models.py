from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    job = models.CharField(max_length=124)
    company = models.CharField(max_length=64)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatar_image/')
    password = models.CharField()


class Contact(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="contact_user")
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Contact of {self.user}"


class Project(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="project_user")
    project_image = models.ImageField(upload_to='image_project/')
    project_name = models.CharField(max_length=124)
    project_description = models.TextField()
    follow = models.URLField()


