from django.urls import path
from accounts import views

# Set the app namespace for URL reversing
app_name='accounts'

# URL patterns for the accounts app (login and registration)
urlpatterns=[
    path('login/',views.login_view,name='login_view'),
    path('registration/',views.register_user,name='register_user') 
]
