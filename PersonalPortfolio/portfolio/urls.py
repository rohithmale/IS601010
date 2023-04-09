from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
]