from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsapp.urls')),
    path('', include('accounts.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('port/',include("Portfolio.urls")),
]
