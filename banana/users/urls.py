from django.urls import path, include
from . import views
from users.views import Register

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]