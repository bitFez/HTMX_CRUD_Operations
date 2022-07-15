from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.home, name='home'),
    path('daily-checkin/', views.daily_checkin, name='daily_checkin'),
    path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]
