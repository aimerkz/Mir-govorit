from django.contrib import admin

from api.models import Product, Recipe, RecipeProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number_of_uses', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    empty_value_display = 'empty'
    list_per_page = 20


class ProductInlineAdmin(admin.StackedInline):
    model = RecipeProduct
    extra = 5


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    inlines = (ProductInlineAdmin,)
    autocomplete_fields = ('products',)
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    empty_value_display = 'empty'
    list_per_page = 20


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_id', 'product_weight',
        'recipe_id', 'created_at', 'updated_at'
    )
    list_select_related = (
        'product_id',
        'recipe_id',
    )
    list_editable = ('product_id', 'product_weight')
    list_filter = ('created_at', 'updated_at')
    empty_value_display = 'empty'
    list_per_page = 20
