from django.urls import path
from app1 import views

urlpatterns = [
    path('api/', views.All_information_without_rest.as_view()),
]