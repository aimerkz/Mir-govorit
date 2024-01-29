from rest_framework import status
from rest_framework.exceptions import APIException


class RecipeException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Рецепт не найден'


class ProductException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Продукт не найден'


class RecipeProductException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Продукт в рецепте не найден'
