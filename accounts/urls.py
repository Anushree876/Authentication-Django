from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    
    path('', views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout")
]
