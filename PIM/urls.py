from django.conf.urls import include, url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'settings' , settingsViewSet , base_name = 'settings')
router.register(r'theme' , themeViewSet , base_name = 'theme')
router.register(r'notification' , notificationViewSet, base_name = 'notification')
router.register(r'chatMessage' , chatMessageViewSet, base_name = 'chatmessage')
router.register(r'chatMessageBetween' , chatMessageBetweenViewSet, base_name = 'chatbetween')

urlpatterns = [
    url(r'^', include(router.urls)),
]
