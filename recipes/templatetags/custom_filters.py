from django import template
from pprint import pprint

register = template.Library()


def resize_to(ingredient, target):
    # Get the number of servings from the ingredient's
    # recipe using the ingredient.recipe.servings
    # properties
    pprint(ingredient)
    servings = ingredient.recipe.servings
    amount = ingredient.amount

    # If the servings from the recipe is not None
    if servings is not None and target is not None:
        #   and the value of target is not None
        # try
        try:
            # calculate the ratio of target over
            #   servings
            ratio = int(target) / int(servings)
            # return the ratio multiplied by the
            #   ingredient's amount
            servings = ratio * amount
            return servings
        # catch a possible error
        except ValueError:
            # pass
            pass

    # return the original ingredient's amount since
    #   nothing else worked
    return amount


register.filter(resize_to)
