from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from tags.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin


"""DELETED SHOW_TAGS FUNCTION - switching to ListView
# Create your views here.
def show_tags(request):
    context = {
        "tags": Tag.objects.all() if Tag else None,
    }
    return render(request, "tags/list.html", context)"""


class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"
    paginate_by = 2


class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = "tags/detail.html"


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("recipes_list")


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name", "recipes"]

    def get_success_url(self):
        return reverse_lazy("tag_detail", kwargs={"pk": self.object.pk})


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "tags/delete.html"

    success_url = reverse_lazy("tags_list")
