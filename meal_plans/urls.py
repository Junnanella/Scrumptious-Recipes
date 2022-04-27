from django.urls import path

from meal_plans.views import (
    MealPlanCreateView,
    MealPlanDeleteView,
    MealPlanUpdateView,
    MealPlanDetailView,
    MealPlanListView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="mealplan_list"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="mealplan_detail"),
    path("new/", MealPlanCreateView.as_view(), name="mealplan_new"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="mealplan_edit"),
    path("<int:pk>/delete/", MealPlanDeleteView.as_view(), name="mealplan_delete"),
]
