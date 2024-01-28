from django.db.models import F

from api.exceptions import ProductException, RecipeException
from api.models import Product, Recipe, RecipeProduct


class RepoAdapter:

    def __init__(self, recipe_id: int | None, product_id: int | None):
        self.recipe_id = recipe_id
        self.product_id = product_id

    def get_recipe(self) -> Recipe:
        try:
            return Recipe.objects.get(id=self.recipe_id)
        except Recipe.DoesNotExist:
            raise RecipeException()

    def get_product(self) -> Product:
        try:
            return Product.objects.get(id=self.product_id)
        except Product.DoesNotExist:
            raise ProductException()


class UpdateService:

    def __init__(self, recipe: Recipe | None, product: Product | None):
        self.product = product
        self.recipe = recipe

    def plus_number_of_uses_product(self) -> None:
        return self.recipe.products.update(number_of_uses=F('number_of_uses') + 1)

    def add_product_to_recipe(self, weight: int) -> None:
        return RecipeProduct.objects.create(product_id=self.product, recipe_id=self.recipe, product_weight=weight)
