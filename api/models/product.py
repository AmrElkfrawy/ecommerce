from django.db import models
from django.core.validators import MinValueValidator
from api.models.category import Category
from django.contrib.auth import get_user_model
from api.models.audit import Audit
from api.constants import CURRENCY_CHOICES


User = get_user_model()


class Product(Audit):
    """
    Model representing a product.

    Fields:
        name: The name of the product.
        price: The price of the product.
        description: The description of the product.
        image: The image of the product.
        count: The count of the product.
        category: The category of the product.
        currency: The currency of the product.
        created_by: The user who created the product.
    """

    name = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="api/images/")
    count = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="products"
    )

    def __str__(self):
        return self.name
