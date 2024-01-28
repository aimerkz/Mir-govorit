from django.urls import path

from api.views import add_product_to_recipe, cook_recipe

urlpatterns = [
    path('cook_recipe/<int:recipe_id>/', cook_recipe, name='cook_recipe'),
    path(
        'add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/',
        add_product_to_recipe, name='add_product_to_recipe'
    ),
]
