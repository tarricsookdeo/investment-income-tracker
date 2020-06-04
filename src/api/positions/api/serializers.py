from rest_framework.serializers import ModelSerializer

from positions.models import Position


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
