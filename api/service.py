from django.db.models import F, Q, QuerySet, Subquery

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

    def get_recipe_product(self) -> QuerySet[RecipeProduct]:
        return RecipeProduct.objects.filter(product_id=self.product_id)

    def get_recipes_without_product(self) -> QuerySet[Recipe]:
        recipe_products_lt_10 = self.get_recipe_product().filter(product_weight__lt=10).values('recipe_id')
        return Recipe.objects.filter(~Q(products__id=self.product_id) | Q(pk__in=Subquery(recipe_products_lt_10)))


class UpdateService:

    def __init__(self, recipe: Recipe | None, product: Product | None):
        self.product = product
        self.recipe = recipe

    def plus_number_of_uses_product(self) -> None:
        return self.recipe.products.update(number_of_uses=F('number_of_uses') + 1)

    def add_product_to_recipe(self, weight: int) -> None:
        return RecipeProduct.objects.create(product_id=self.product, recipe_id=self.recipe, product_weight=weight)
