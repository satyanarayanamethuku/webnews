
from .views import greet, display_view
from django.urls import path

urlpatterns = [
  path('hello/',greet),
  path('first/',display_view),
]