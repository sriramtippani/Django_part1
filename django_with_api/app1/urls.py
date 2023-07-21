from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.homepage_view),
    path('hydjob/', views.hydJobs_view),
    path('banglorejob/', views.bloreJobs_view),
    path('chennaijob/', views.chennaiJobs_view),
    path('punejob/', views.puneJobs_view),
    path('register/', views.register_request, name='register'),
    # path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
]
