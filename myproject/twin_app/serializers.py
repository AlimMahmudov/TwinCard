from rest_framework import serializers
from .models import *


class TelegramSerializers(serializers.ModelSerializer):
    class Meta:
        model = Telegram
        fields = ['id', 'telegram']


class InstagramSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = ['id', 'instagram']


class WhatsappSerializers(serializers.ModelSerializer):
    class Meta:
        model = Whatsapp
        fields = ['id', 'whatsapp']


class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'phone']


class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'email']


class LinkedinSerializers(serializers.ModelSerializer):
    class Meta:
        model = Linkedin
        fields = ['id', 'linkedin']

class ProjectImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class ProjectSerializers(serializers.ModelSerializer):
    images = ProjectImageSerializers(read_only=True, many=True)
    class Meta:
        model = Project
        fields = ['id', 'images', 'project_name', 'project_description', 'follow']


class UseProfileSerializers(serializers.ModelSerializer):
    telegram_user = TelegramSerializers(read_only=True, many=True)
    instagram_user = InstagramSerializers(read_only=True, many=True)
    whatsapp_user = WhatsappSerializers(read_only=True, many=True)
    phone_user = PhoneSerializers(read_only=True, many=True)
    email_user = EmailSerializers(read_only=True, many=True)
    linkedin_user = LinkedinSerializers(read_only=True, many=True)
    project_user = ProjectSerializers(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'username',
            'job',
            'company',
            'description',
            'avatar',
            'password',
            'telegram_user',
            'instagram_user',
            'whatsapp_user',
            'phone_user',
            'email_user',
            'linkedin_user',
            'project_user'
        ]
