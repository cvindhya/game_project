from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register_request,name="register"),
    path('home', views.homepage, name='home'),
]