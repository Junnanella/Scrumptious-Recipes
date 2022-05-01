from django.shortcuts import redirect
from recipes.forms import RatingForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db import IntegrityError

from recipes.models import Recipe, ShoppingItem, Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try:
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
            except Recipe.DoesNotExist:
                return redirect("recipes_list")
    return redirect("recipe_detail", pk=recipe_id)


# UPDATE: SWITCH TO USING CLASSES BELOW:


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 2


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()

        # Create a new empty list and assign it to a variable
        foods = []

        # For each item in the user's shopping items, which we
        # can access through the code
        users_items = self.request.user.shopping_item.all()

        for item in users_items:
            # Add the shopping item's food to the list
            foods.append(item.food_item.name)

        # Put that list into the context
        context["food_in_shopping_list"] = foods
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = [
        "name",
        "description",
        "image",
        "servings",
    ]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = [
        "name",
        "description",
        "image",
    ]
    success_url = reverse_lazy("recipes_list")


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")


class ShoppingListView(LoginRequiredMixin, ListView):
    model = ShoppingItem
    template_name = "recipes/shoppinglist.html"
    context_object_name = "shopping_list"

    # Filter to only show shopping list to corresponding logged in user
    def get_queryset(self):
        return ShoppingItem.objects.filter(user=self.request.user)


def create_shopping_item(request):
    # Get the value for the "ingredient_id" from the
    # request.POST dictionary using the "get" method
    ingredient_id = request.POST.get("ingredient_id")

    # Get the specific ingredient from the Ingredient model
    # using the code
    # Ingredient.objects.get(id=the value from the dictionary)
    ingredient = Ingredient.objects.get(id=ingredient_id)

    # Get the current user which is stored in request.user
    user = request.user

    try:
        # Create the new shopping item in the database
        ShoppingItem.objects.create(food_item=ingredient.food_item, user=user)
    except IntegrityError:
        pass

    # Go back to the recipe page with a redirect
    # to the name of the registered recipe detail
    # path with code like this
    # return redirect(
    #     name of the registered recipe detail path,
    #     pk=id of the ingredient's recipe
    # )
    return redirect("recipe_detail", pk=ingredient.recipe.id)


def delete_shopping_list(request):
    # Delete all of the shopping items for the user
    # using code like
    ShoppingItem.objects.filter(user=request.user).delete()

    # Go back to the shopping item list with a redirect
    # to the name of the registered shopping item list
    # path with code like this
    return redirect("shopping_item_list")
