from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(verbose_name='Название продукта', blank=False, null=False, max_length=100)
    number_of_uses = models.IntegerField(verbose_name='Количество использований в рецептах', default=0)

    objects = models.Manager()

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Recipe(BaseModel):
    name = models.CharField(verbose_name='Название рецепта', blank=False, null=False, max_length=250)
    products = models.ManyToManyField('api.Product', through='RecipeProduct', verbose_name='Продукты в рецепте')

    objects = models.Manager()

    class Meta:
        db_table = 'recipe'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeProduct(BaseModel):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='recipe_product')
    product_weight = models.PositiveIntegerField(verbose_name='Вес продукта в граммах', default=1)
    recipe_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        db_table = 'recipe_product'
        verbose_name = 'Продукт в рецепте'
        verbose_name_plural = 'Продукты в рецепте'
        unique_together = [['product_id', 'recipe_id']]
