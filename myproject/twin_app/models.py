from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    job = models.CharField(max_length=124)
    company = models.CharField(max_length=64)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatar_image/')
    password = models.CharField(max_length=255, default="123456789")


class Telegram(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="telegram_user")
    telegram = models.URLField(null=True, blank=True)


class Instagram(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="instagram_user")
    instagram = models.URLField(null=True, blank=True)


class Whatsapp(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="whatsapp_user")
    whatsapp = models.URLField(null=True, blank=True)


class Phone(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="phone_user")
    phone = models.PositiveSmallIntegerField(null=True, blank=True)


class Email(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="email_user")
    email = models.EmailField(null=True, blank=True)


class Linkedin(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="linkedin_user")
    linkedin = models.URLField(null=True, blank=True)


class Project(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="project_user")
    project_name = models.CharField(max_length=124)
    project_description = models.TextField()
    follow = models.URLField()


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="images")
    project_image = models.ImageField(upload_to='image_project/')

