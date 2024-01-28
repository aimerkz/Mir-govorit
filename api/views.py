from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from api.service import RepoAdapter, UpdateService


@api_view(['GET'])
def cook_recipe(request: Request, recipe_id: int) -> Response:
    """
    Функция для увеличения на 1 количества приготовленных блюд для каждого продукта
    """
    recipe = RepoAdapter(recipe_id, None).get_recipe()
    UpdateService(recipe=recipe, product=None).plus_number_of_uses_product()
    return Response(status=HTTP_200_OK, data='Success!')


@api_view(['GET'])
def add_product_to_recipe(request: Request, recipe_id: int, product_id: int, weight: int) -> Response:
    """
    Добавление продукта и его веса в рецепт
    """
    recipe, product = RepoAdapter(recipe_id, None).get_recipe(), RepoAdapter(None, product_id).get_product()
    UpdateService(recipe, product).add_product_to_recipe(weight)
    return Response(status=HTTP_201_CREATED, data='Success!')
