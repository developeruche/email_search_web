from django.urls import path
from .views import index, ReceiveString, ReceiveImage
urlpatterns = [
    path("", index, name='home'),
    path("submit_string", ReceiveString, name="submit_string"),
    path("submit_string", ReceiveImage, name="submit_image"),
]
