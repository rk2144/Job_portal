from django.urls import path
from . import views



urlpatterns=[
    path('',views.index,name='index'),
    path('elements/',views.elements,name='elements'),
    path('blog/',views.blog,name='blog'),
  
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about,name="about"),
    path('job_details/',views.job_details,name='job_details'),
    path('job_listing/',views.job_listing,name='job_listing'),
    path('blog/',views.blog,name="blog"),
    path('search/',views.search,name='search'),
    path('singal_blog/',views.singal_blog,name="singal_blog")
    

]