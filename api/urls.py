from django.urls import path
from . import views

urlpatterns = [
    path("slider_image", views.getSliderImage, name="getSliderImage"),
]
