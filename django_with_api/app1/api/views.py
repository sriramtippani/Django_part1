from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app1.api.serializers import HydAPI
from app1.models import hydjobs
from rest_framework.pagination import PageNumberPagination
from app1.api.pagination import MyPagination


class HydCRUDCBV(ModelViewSet):
    queryset = hydjobs.objects.all()
    serializer_class = HydAPI
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    pagination_class = MyPagination
    search_fields = ('company', )
