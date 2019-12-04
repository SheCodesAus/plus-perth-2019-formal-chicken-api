
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'profiles', views.ProfileViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]