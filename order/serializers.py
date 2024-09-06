from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'bimar', 'service', 'price', 'date']