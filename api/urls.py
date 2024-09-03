from django.urls import path, include


from .views.category import (
    CategoryListView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryProductListView,
)
from .views.order import (
    OrderListView,
    OrderCancelView,
    OrderTrackView,
    OrderCreateView,
    OrderDeliverView,
)

from .views.cart import (
    AddToCartView,
    RemoveFromCartView,
    ClearCartView,
    UpdateCartItemView,
    CartView,
)

from .views import (
    UserRegisterView,
    UserLoginView,
    VerifyOTPView,
    RefreshTokenView,
    ForgotPasswordView,
    PasswordResetView,
    UpdatePasswordView,
    ProfileDetailView,
    ProfileUpdateView,
    PaymentListView,
    PaymentDetailView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    WishlistListView,
    WishlistItemCreateView,
    WishlistItemDeleteView,
    WishlistDeleteView,
)

from .views.product import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

from .views.review import (
    GetReviewsByProductView,
    CreateReviewView,
    UpdateReviewView,
    DeleteReviewView,
)

category_patterns = [
    path("", CategoryListView.as_view(), name="list"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete"),
    path(
        "<int:category_pk>/products/",
        CategoryProductListView.as_view(),
        name="products",
    ),
]
order_patterns = [
    path("", OrderListView.as_view(), name="list"),
    path("<int:pk>/cancel/", OrderCancelView.as_view(), name="cancel"),
    path("<int:pk>/track/", OrderTrackView.as_view(), name="track"),
    path("orders/create/", OrderCreateView.as_view(), name="create"),
    path("<int:pk>/deliver/", OrderDeliverView.as_view(), name="deliver"),
]

user_patterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path(
        "password-reset/<str:token>/",
        PasswordResetView.as_view(),
        name="password-reset",
    ),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("refresh-token/", RefreshTokenView.as_view(), name="refresh-token"),
    path("me/", ProfileDetailView.as_view(), name="profile-detail"),
    path("me/update/", ProfileUpdateView.as_view(), name="profile-update"),
    path("verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),
    path("update-password/", UpdatePasswordView.as_view(), name="update-password"),
]

payment_patterns = [
    path("", PaymentListView.as_view(), name="payment-list"),
    path("create/", PaymentCreateView.as_view(), name="payment-create"),
    path("<int:payment_id>/", PaymentDetailView.as_view(), name="payment-detail"),
    path(
        "update/<int:payment_id>/", PaymentUpdateView.as_view(), name="payment-update"
    ),
    path(
        "delete/<int:payment_id>/", PaymentDeleteView.as_view(), name="payment-delete"
    ),
]

wishlist_patterns = [
    path("", WishlistListView.as_view(), name="wishlist-list"),
    path(
        "items/create/", WishlistItemCreateView.as_view(), name="wishlist-item-create"
    ),
    path(
        "items/delete/<int:item_id>",
        WishlistItemDeleteView.as_view(),
        name="wishlist-item-delete",
    ),
    path("clear/", WishlistDeleteView.as_view(), name="wishlist-clear"),
]

product_patterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:product_id>/", ProductDetailView.as_view(), name="product-detail"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path(
        "update/<int:product_id>/", ProductUpdateView.as_view(), name="product-update"
    ),
    path(
        "delete/<int:product_id>/", ProductDeleteView.as_view(), name="product-delete"
    ),
]

cart_patterns = [
    path("", CartView.as_view(), name="cart"),
    path("add/", AddToCartView.as_view(), name="add-to-cart"),
    path(
        "remove/<int:item_id>/", RemoveFromCartView.as_view(), name="remove-from-cart"
    ),
    path("clear/", ClearCartView.as_view(), name="clear-cart"),
    path(
        "update/<int:item_id>/", UpdateCartItemView.as_view(), name="update-cart-item"
    ),
]

review_patterns = [
    path(
        "products/<int:product_id>/",
        GetReviewsByProductView.as_view(),
        name="product-reviews",
    ),
    path(
        "products/<int:product_id>/create/",
        CreateReviewView.as_view(),
        name="create-review",
    ),
    path("update/<int:review_id>", UpdateReviewView.as_view(), name="update-review"),
    path(
        "delete/<int:review_id>",
        DeleteReviewView.as_view(),
        name="delete-review",
    ),
]

urlpatterns = [
    path("categories/", include((category_patterns, "categories"))),
    path("orders/", include((order_patterns, "orders"))),
    path("users/", include(user_patterns)),
    path("payments/", include(payment_patterns)),
    path("wishlists/", include(wishlist_patterns)),
    path("products/", include(product_patterns)),
    path("carts/", include(cart_patterns)),
    path("reviews/", include(review_patterns)),
]
