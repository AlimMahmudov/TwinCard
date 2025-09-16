from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),

    # Project
    path('project/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-list'),
    path('project/<int:pk>/', ProjectViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='project-detail'),

    # Telegram
    path('telegram/', TelegramViewSet.as_view({'get': 'list', 'post': 'create'}), name='telegram-list'),
    path('telegram/<int:pk>/', TelegramViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='telegram-detail'),

    # Instagram
    path('instagram/', InstagramViewSet.as_view({'get': 'list', 'post': 'create'}), name='instagram-list'),
    path('instagram/<int:pk>/', InstagramViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='instagram-detail'),

    # Whatsapp
    path('whatsapp/', WhatsappViewSet.as_view({'get': 'list', 'post': 'create'}), name='whatsapp-list'),
    path('whatsapp/<int:pk>/', WhatsappViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='whatsapp-detail'),

    # Phone
    path('phone/', PhoneViewSet.as_view({'get': 'list', 'post': 'create'}), name='phone-list'),
    path('phone/<int:pk>/', PhoneViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='phone-detail'),

    # Email
    path('email/', EmailViewSet.as_view({'get': 'list', 'post': 'create'}), name='email-list'),
    path('email/<int:pk>/', EmailViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='email-detail'),

    # Linkedin
    path('linkedin/', LinkedinViewSet.as_view({'get': 'list', 'post': 'create'}), name='linkedin-list'),
    path('linkedin/<int:pk>/', LinkedinViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='linkedin-detail'),
]

