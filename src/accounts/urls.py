from django.urls import path
from accounts import views
app_name='accounts'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('registration/',views.register,name='register') 
]
