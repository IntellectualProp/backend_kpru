from django.urls import path
from . import views

urlpatterns = [
    path("slider_image", views.getSliderImage, name="getSliderImage"),
    path("ip_knowledge", views.getIpKnowledge, name="getIpKnowledge"),
]
