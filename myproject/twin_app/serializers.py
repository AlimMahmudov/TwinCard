from rest_framework import serializers
from .models import *

class UseProfileSerializers(serializers.ModelSerializer):
   class Meta:
      model = UserProfile
      fields = ['id', 'username', 'job', 'company', 'description', 'avatar', 'password']


class ContactSerializers(serializers.ModelSerializer):
    user = UseProfileSerializers(read_only=True)

    class Meta:
        model = Contact
        fields = ['user', 'telegram', 'instagram', 'whatsapp', 'phone', 'email', 'linkedin']


class ProjectSerializers(serializers.ModelSerializer):
    user = UseProfileSerializers(read_only=True)

    class Meta:
      model = Project
      fields = ['id', 'project_image', 'project_name', 'project_description', 'follow', 'user']