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

# from recipes.forms import RecipeForm
from recipes.models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin


"""DELETED CREATE_RECIPE FUNCTION - switching to a CreateView
def create_recipe(request):
    if request.method == "POST" and RecipeForm:
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipe_detail", pk=recipe.pk)
    elif RecipeForm:
        form = RecipeForm()
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/new.html", context)"""

"""DELETED CHANGE_RECIPE FUNCTION - switching to a UpdateView
def change_recipe(request, pk):
    if Recipe and RecipeForm:
        instance = Recipe.objects.get(pk=pk)
        if request.method == "POST":
            form = RecipeForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect("recipe_detail", pk=pk)
        else:
            form = RecipeForm(instance=instance)
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/edit.html", context)"""

"""DELETED SHOW_RECIPES FUNCTION - switching to a ListView
def show_recipes(request):
    context = {
        "recipes": Recipe.objects.all() if Recipe else [],
    }
    return render(request, "recipes/list.html", context)"""

"""DELETED SHOW_RECIPE FUNCTION - switching to a DetailView
def show_recipe(request, pk):
    context = {
        "recipe": Recipe.objects.get(pk=pk) if Recipe else None,
        "rating_form": RatingForm(),
    }
    return render(request, "recipes/detail.html", context)"""


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
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = [
        "name",
        "description",
        "image",
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
