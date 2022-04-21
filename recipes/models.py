from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """the __str__ method, is what gets called by Python when it wants to turn
    it into a string. You can use any of the properties
    that you defined in the __str__ method."""

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.abbreviation


class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE,
        null=True,
    )
    measure = models.ForeignKey(
        "Measure", related_name="ingredients", on_delete=models.PROTECT
    )
    food_item = models.ForeignKey(
        "FoodItem", related_name="ingredients", on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.amount} + {self.measure} + {self.food_item}"


class Step(models.Model):
    recipe = models.ForeignKey(
        "Recipe", related_name="steps", on_delete=models.CASCADE, null=True
    )
    order = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.order} + {self.directions}"


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    recipe = models.ForeignKey(
        "Recipe", related_name="ratings", on_delete=models.CASCADE
    )
