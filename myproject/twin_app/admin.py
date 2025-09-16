from django.contrib import admin
from .models import *


# Соцсети
class TelegramInline(admin.TabularInline):
    model = Telegram
    extra = 1


class InstagramInline(admin.TabularInline):
    model = Instagram
    extra = 1


class WhatsappInline(admin.TabularInline):
    model = Whatsapp
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class LinkedinInline(admin.TabularInline):
    model = Linkedin
    extra = 1


# Внутри Project добавляем ProjectImage
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


# Админка для проекта
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]


# Админка для пользователя
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [
        TelegramInline,
        InstagramInline,
        WhatsappInline,
        PhoneInline,
        EmailInline,
        LinkedinInline,
    ]


# Регистрируем модели
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, ProjectAdmin)
