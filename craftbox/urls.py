from django.urls import path

# from . import views
from .views import (
    LinkListView,
    LinkDetailView,
    LinkUpdateView,
    LinkDeleteView,
    LinkCreateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDetailView,
    TagDeleteView,
)

urlpatterns = [
    path("new/", LinkCreateView.as_view(), name="link_new"),
    path("", LinkListView.as_view(), name="link_list"),
    path("<uuid:pk>", LinkDetailView.as_view(), name="link_detail"),
    path("<uuid:pk>/edit", LinkUpdateView.as_view(), name="link_edit"),
    path("<uuid:pk>/delete", LinkDeleteView.as_view(), name="link_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/new/", TagCreateView.as_view(), name="tag_new"),
    path("tags/<int:pk>/detail", TagDetailView.as_view(), name="tag_detail"),
    path("tags/<int:pk>/edit", TagUpdateView.as_view(), name="tag_edit"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag_delete"),
]
