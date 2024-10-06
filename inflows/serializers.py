from rest_framework.serializers import ModelSerializer
from .models import Inflow


class InflowSerializer(ModelSerializer):
    class Meta:
        model = Inflow
        fields = '__all__'
