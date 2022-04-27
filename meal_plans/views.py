from audioop import reverse
from django.shortcuts import redirect
from meal_plans.models import MealPlan
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class MealPlanListView(ListView):
    model = MealPlan
    template_name = "meal_plans/list.html"
    paginate_by = 2


class MealPlanDetailView(DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/new.html"
    fields = ["name", "recipes", "date"]

    success_url = reverse_lazy("mealplan_detail", "mealplan.pk")

    def form_valid(self, form):
        mealplan = form.save(commit=False)
        mealplan.owner = self.request.user
        mealplan.save()
        form.save_m2m()
        return redirect("mealplan_detail", pk=mealplan.id)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    fields = ["name", "recipes", "date"]

    def form_valid(self, form):
        mealplan = form.save(commit=False)
        mealplan.owner = self.request.user
        mealplan.save()
        form.save_m2m()
        return redirect("mealplan_detail", pk=mealplan.id)

class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("mealplan_list")
