from django.urls import path
from .views import encode_message
from . import views

urlpatterns = [
	path('', encode_message, name='crypto'),
]