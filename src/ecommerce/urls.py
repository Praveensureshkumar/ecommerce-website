"""
URL configuration for ewebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ecommerce.views import *
from products.views import *
from orders.views import *
from accounts.views import *
from dashboard.views import *
import accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('ecommerce/',ecommerce,name='ecommerce'),
    path('ecommerce/<str:category>/',ecommerce,name='category_products'),
    path('full_product/<int:product_id>/',full_product,name='full_product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_cart/<int:cart_item_id>/', remove_cart, name='remove_cart'),
    path('logout/',logout_view, name='logout'),
    path('checkout/',checkout,name='checkout'),
    path('cart/',cart,name='cart'),
    path('profile/', profile_update_view, name='profile'),
    path('delete-account/',delete_account, name='delete_account'),
    path('', home, name='home'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

