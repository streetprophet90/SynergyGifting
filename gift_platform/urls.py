"""
URL configuration for gift_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from users import views as user_views
from wishlist import views as wishlist_views
from orders import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('wishlist/', wishlist_views.wishlist, name='wishlist'),
    path('wishlist/add/', wishlist_views.add_item, name='add_item'),
    path('wishlist/<slug:slug>/', wishlist_views.public_wishlist, name='public_wishlist'),
    path('order/<int:item_id>/', order_views.place_order, name='place_order'),
    path('order/<int:item_id>/<slug:slug>/', order_views.place_order, name='place_order_from_public'),
    path('order_confirmation/', order_views.order_confirmation, name='order_confirmation'),
    path('', user_views.home, name='home'),
]





