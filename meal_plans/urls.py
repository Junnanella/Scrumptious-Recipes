from django.urls import path

from meal_plans.views import (
    # MealPlanCreateView,
    # MealPlanDeleteView,
    # MealPlanUpdateView,
    # MealPlanDetailView,
    MealPlanListView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_plans_list"),
    # path("", MealPlanDetailView.as_view(), name="meal_plan_detail"),
    # path("", MealPlanCreateView.as_view(), name="meal_plan_new"),
    # path("", MealPlanUpdateView.as_view(), name="meal_plan_edit"),
    # path("", MealPlanDeleteView.as_view(), name="meal_plan_delete"),
]
