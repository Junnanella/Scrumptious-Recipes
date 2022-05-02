from ast import In
from sre_constants import IN
from unittest import TestCase
from recipes.models import Ingredient, Recipe
from recipes.templatetags.custom_filters import resize_to


class ResizeToTests(TestCase):
    def test_error_when_ingredient_is_none(self):
        # Arrange - we have nothing to arrange, so this stays blank

        # Act - to test for an error, we use the assertRaises method
        with self.assertRaises(AttributeError):
            resize_to(None, 3)

        # Assert

    def test_recipe_has_no_serving(self):
        # Arrange - for an Ingredient with a Recipe whose servings property is None
        # The Ingredient's amount needs to be some value, which in our example is 5
        recipe = Recipe(servings=None)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act - Calling the resize_to function and getting the result
        #
        #                   |the ingredient value that we created
        #                   |          |the target value from the table
        #                   v          v
        result = resize_to(ingredient, None)

        # Assert - Use the assertEqual method with the expected result, 5
        self.assertEqual(5, result)

    def test_resize_to_is_none(self):
        # Arrange - arrange the data according to appropriate valuse for the test
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act - by calling the resize_to function
        result = resize_to(ingredient, None)

        # Assert - the result is what we expected
        self.assertEqual(5, result)

    def test_values_for_servings_amount_and_target(self):
        # Arrange
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act
        result = resize_to(ingredient, 10)

        # Assert
        self.assertEqual(25, result)

    def test_target_is_letters(self):
        # Arrange
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act
        result = resize_to(ingredient, "abc")

        # Assert
        self.assertEqual(5, result)
