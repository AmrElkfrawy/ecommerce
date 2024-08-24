from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from api.selectors.wishlist import (
    get_wishlist_by_user,
)

from api.services.wishlist import (
    add_item_to_wishlist,
    delete_item_from_wishlist,
    clear_wishlist,
)
from api.serializers import (
    WishlistSerializer,
    WishlistItemSerializer,
    WishlistItemCreateSerializer,
)


class WishlistListView(APIView):
    """Api view for the wishlist"""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Handle GET request for user's wishlist
        Returns:
            Response object containing the wishlist data.
        """
        wishlist = get_wishlist_by_user(request.user)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WishlistDeleteView(APIView):
    """Api view for clearing a wishlist"""

    permission_classes = [IsAuthenticated]

    def delete(self, request):
        """Handle DELETE request to clear a wishlist
        Returns:
            Response object containing the cleared wishlist data.
        """
        wishlist = get_wishlist_by_user(request.user)
        wishlist = clear_wishlist(wishlist)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.exceptions import ValidationError


class WishlistItemCreateView(APIView):
    """API view for creating a wishlist item"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Handle POST request to create a wishlist item
        Returns:
            Response object containing the created wishlist item data.
        """
        wishlist = get_wishlist_by_user(request.user)
        serializer = WishlistItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data.get("product_id")

        try:
            wishlist = add_item_to_wishlist(wishlist, product)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WishlistItemDeleteView(APIView):
    """Api view for deleting a wishlist item"""

    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        """Handle DELETE request to delete a wishlist item
        Returns:
            Response object containing the deleted wishlist item data.
        """
        wishlist = get_wishlist_by_user(request.user)
        try:
            wishlist = delete_item_from_wishlist(wishlist, item_id)
            print("afasf")
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)