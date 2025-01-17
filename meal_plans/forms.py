from django import forms
from meal_plans.models import MealPlan


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ["name", 
        "recipes"
        "date"]
