from django.views.generic import ListView

try:
    from tags.models import Tag
except Exception:
    Tag = None


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
