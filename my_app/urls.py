from django.urls import path
from my_app import views

urlpatterns=[
    path('register',views.register_request,name="register"),
    path('home', views.homepage, name='home'),
]