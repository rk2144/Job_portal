from django.urls import path
from . import views

urlpatterns = [
    path('',views.Port_home, name='Port_home'),
]
