from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),

    # Полный CRUD для Contact
    path('contact/', ContactViewSet.as_view({'get': 'list', 'post': 'create'}), name='contact-list'),
    path('contact/<int:pk>/', ContactViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='contact-detail'),

    # Полный CRUD для Project
    path('project/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-list'),
    path('project/<int:pk>/', ProjectViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='project-detail'),
]
