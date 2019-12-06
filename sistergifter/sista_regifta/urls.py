
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileView)
router.register(r'user', views.UserViewSet)
router.register(r'gift', views.GiftView)    
router.register(r'swap', views.SwapView)   


urlpatterns = [
    path('', include(router.urls)),
]