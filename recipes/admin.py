from django.contrib import admin
from recipes.models import Recipe, Measure

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    pass


class MeasureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Measure, MeasureAdmin)
