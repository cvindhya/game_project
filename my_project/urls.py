from django.contrib import admin 
from django.urls import path,include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',LoginView.as_view(), name='login'),
    path('login',include('my_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
]
