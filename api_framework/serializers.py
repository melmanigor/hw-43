from rest_framework import serializers
from clothing.models import ClothingModel

class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingModel
        fields = '__all__'