from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=225)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)