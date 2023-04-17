from django.contrib import admin
from recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
        "description",


    )

# Register your models here.
