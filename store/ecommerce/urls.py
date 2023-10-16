from django.urls import path
from . import views

urlpatterns = [
    path('api/carts/add', views.AddCart.as_view(), name="add-to-cart"),
    path('api/carts/details/<int:user_id>', views.GetCart.as_view(), name="view-cart"),
    path('api/carts/delete/<int:cart_item_id>', views.DeleteCart.as_view(), name="view-cart"),
]