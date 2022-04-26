from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# try:
from tags.models import Tag

# except Exception:
#     Tag = None


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


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"


class TagCreateView(CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name"]
    success_url = reverse_lazy("recipes_list")
