# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from authentication.views import custom_logout


# Define URL patterns
urlpatterns = [
    path('home/', home, name="recipes"),      # Home page
    
    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
    path('logout/', custom_logout, name='logout'),
]

