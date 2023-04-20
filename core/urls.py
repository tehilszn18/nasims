from django.urls import path
from .views import HomeView, ContactView, NewsView, AboutView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('contact/', ContactView.as_view(), name= 'news'),
    path('news/', NewsView.as_view(), name= 'news'),
    path('about/', AboutView.as_view(), name= 'about')
]