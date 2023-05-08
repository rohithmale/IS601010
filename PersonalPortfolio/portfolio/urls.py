from django.urls import path
from . views import home, portfolio, about, form_view, register_user, login_view, logout_view

urlpatterns = [
    path('home/', home, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('about/', about, name='about'),
    path('form/', form_view, name='form'),
    path('signup/',register_user, name='signup'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout')

]