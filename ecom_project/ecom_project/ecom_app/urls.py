from django.urls import path

from .views import add_product,view_all_products,delete_by_id,add_to_cart,update_product,remove_from_cart,view_cart

urlpatterns = [
    path("add_product",add_product),
    path("view_all_products/",view_all_products),
    path(
        "delete_by_id/<int:id>/",
        delete_by_id,
        name="delete_by_id"
    ),
path("add_to_cart/<int:product_id>/", add_to_cart),
path("update_product/<int:id>/", update_product),
path("remove_from_cart/<int:id>/", remove_from_cart),
path("view_cart/", view_cart),
]