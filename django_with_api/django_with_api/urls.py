"""django_with_api URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', include('app1.urls')),
    path('api_information/', include('app1.api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# By using PostMan application
#-------------------------------
# POST  http://127.0.0.1:8000/api_information/get_api_token/  Send
# in body----> form-data----> username   sriram
#                       ----> password   4194
# The above url pattern for postman tool to generate token for Token Authentication

# http GET http://127.0.0.1:8000/api_information/hydjobAPI/
# then go to Headers----> Key              value
#                         Authorization    Token d9ced921eba226bb49aa1a8b9794fd983ae6253d

# GET  http://127.0.0.1:8000/api_information/hydjobAPI/1/   Send
# then go to Headers----> Key              value
#                         Authorization    Token d9ced921eba226bb49aa1a8b9794fd983ae6253d

# POST  http://127.0.0.1:8000/api_information/hydjobAPI/    Send
# then go to Headers----> Key              value
#                         Authorization    Token d9ced921eba226bb49aa1a8b9794fd983ae6253d

# PUT  http://127.0.0.1:8000/api_information/hydjobAPI/1/    Send
# then go to Headers----> Key              value
#                         Authorization    Token d9ced921eba226bb49aa1a8b9794fd983ae6253d

# PATCH  http://127.0.0.1:8000/api_information/hydjobAPI/1/   Send
# then go to Headers----> Key              value
#                         Authorization    Token d9ced921eba226bb49aa1a8b9794fd983ae6253d

# DELETE  http://127.0.0.1:8000/api_information/hydjobAPI/1/   Send
# then go to Headers----> Key              value
#                         Authorization    Token d9ced921eba226bb49aa1a8b9794fd983ae6253d