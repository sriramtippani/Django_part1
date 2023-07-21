from rest_framework.serializers import ModelSerializer
from app1.models import hydjobs

class HydAPI(ModelSerializer):
    class Meta:
        model = hydjobs
        fields = '__all__'
