from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_pass/', views.changPassword, name='change_pass'),
    path('reset_pass/', views.resetPassword, name='reset_pass'),
]
