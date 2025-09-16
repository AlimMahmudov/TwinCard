from rest_framework import viewsets
from .serializers import *
from .models import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UseProfileSerializers


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class TelegramViewSet(viewsets.ModelViewSet):
    queryset = Telegram.objects.all()
    serializer_class = TelegramSerializers


class InstagramViewSet(viewsets.ModelViewSet):
    queryset = Instagram.objects.all()
    serializer_class = InstagramSerializers


class WhatsappViewSet(viewsets.ModelViewSet):
    queryset = Whatsapp.objects.all()
    serializer_class = WhatsappSerializers


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializers


class LinkedinViewSet(viewsets.ModelViewSet):
    queryset = Linkedin.objects.all()
    serializer_class = LinkedinSerializers
