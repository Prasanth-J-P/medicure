from rest_framework import serializers
from storeroom.models import Medicinedetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicinedetails
        fields = '__all__'