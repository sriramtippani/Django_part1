from django.urls import path, include
from app1 import views

urlpatterns = [
    path('api/', views.All_view_data.as_view()),
]
