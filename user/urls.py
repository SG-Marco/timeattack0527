from django.urls import path
from . import views

urlpatterns = [
    path('user/register', views.sign_up, name='sign-up'),
]