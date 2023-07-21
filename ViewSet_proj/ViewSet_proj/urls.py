"""ViewSet_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from app1.views import E1, E2, E3
from rest_framework.authtoken import views


# for ViewSet setup and Token Authentication included use postman application for operations.
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api_1', E1)
router.register('api_2', E2)
router.register('api_3', E3)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('any_name/', views.obtain_auth_token, name='any_name'), # complusory you should add this for token authentication
]
