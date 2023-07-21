from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home_page),
    path('form/', views.form_page),
    path('submit/', views.confirm_submit),
    path('apiresult/', views.FormCRUDCBV.as_view()),
]
