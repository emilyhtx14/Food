"""foodDonation1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from accounts.views import signup_view,login_view, \
    profile_view, logout_view, create_donation, \
    donation_detail_view,user_view, deliv_one_view, deliv_two_view

app_name = 'accounts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup',signup_view),
    path('accounts/login',login_view),
    path('accounts/profile',profile_view),
    path('accounts/logout',logout_view),
    path('accounts/donate',create_donation),
    path('accounts/deliveries',donation_detail_view),
    path('accounts/userview',user_view),
    path('accounts/delivery1',deliv_one_view),
    path('accounts/delivery2', deliv_two_view)

]
