from django.urls import path

from .views import (
    LinkListView,
    LinkDetailView,
    LinkUpdateView,
    LinkDeleteView,
    LinkCreateView,
)

urlpatterns = [
    path("new/", LinkCreateView.as_view(), name="link_new"),
    path("", LinkListView.as_view(), name="link_list"),
    path("<uuid:pk>", LinkDetailView.as_view(), name="link_detail"),
    path("<uuid:pk>/edit", LinkUpdateView.as_view(), name="link_edit"),
    path("<uuid:pk>/delete", LinkDeleteView.as_view(), name="link_delete"),
]
