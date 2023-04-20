from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import DashboardView, NewProfile, UserRegistration

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('update_profile/<pk>', NewProfile.as_view(), name='update_profile'),
    path('register/', UserRegistration.as_view(), name='register')
]
