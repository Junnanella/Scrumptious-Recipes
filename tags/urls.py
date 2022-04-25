from django.urls import path

from tags.views import TagCreateView, TagListView, TagDetailView, TagCreateView

urlpatterns = [
    path("", TagListView.as_view(), name="tags_list"),
    path("<int:pk>/", TagDetailView.as_view(), name="tag_detail"),
    path("new/", TagCreateView.as_view(), name="tag_new"),
]
