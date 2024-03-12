from django.urls import path
from .views import *

urlpatterns = [
    path('api/login/', LoginView.as_view()),
]