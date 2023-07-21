from django.urls import path, include
from app1.api.views import HydCRUDCBV

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('hydjobAPI', HydCRUDCBV)

from rest_framework.authtoken import views

urlpatterns = [
    path('', include(router.urls)),
    # path('get_api_token/', views.obtain_auth_token, name='get_api_token'),
]
