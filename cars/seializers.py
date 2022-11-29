from rest_framework import serializers

from .models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Brand