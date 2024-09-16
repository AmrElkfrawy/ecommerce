from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.selectors.order import get_order_by_id_and_user, get_orders_by_user


from api.services.order import (
    cancel_order,
    create_order_from_cart,
    mark_order_as_delivered,
)
from api.serializers.order import OrderSerializer, OrderCreateSerializer

from api.models.payment import Payment
from api.models.order import Order

import logging

logger = logging.getLogger(__name__)


class OrderCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        response_data, success = cancel_order(pk, request.user)
        if success:
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class OrderTrackView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = get_order_by_id_and_user(pk, request.user)
        serializer = OrderSerializer(order)
        if serializer.data["user"] == None:
            return Response("No order Found", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = get_orders_by_user(request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDeliverView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        response_data, success = mark_order_as_delivered(pk, request.user)
        if success:
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logger.info(f"Creating order for {request.user.email}")
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        payment_method = serializer.validated_data["payment_method"]

        try:
            order = create_order_from_cart(user=user, payment_method=payment_method)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)


class OrderCreateViewWithDiscount(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        payment_method = serializer.validated_data["payment_method"]
        discount_code = request.discount_price

        try:
            order = create_order_from_cart(
                user=user, payment_method=payment_method, discount_code=discount_code
            )
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
