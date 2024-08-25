from rest_framework import serializers

from api.models.order import Order

from api.serializers.order_item import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "payment_method",
            "status",
            "total_price",
            "items",
            "created_at",
            "updated_at",
        ]