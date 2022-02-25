from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


from .models import Link

# Create your views here.


class LinkListView(LoginRequiredMixin, ListView):
    model = Link
    context_object_name = "link_list"
    template_name = "links/link_list.html"


class LinkDetailView(LoginRequiredMixin, DetailView):
    model = Link
    template_name = "links/link_detail.html"


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    template_name = "links/link_new.html"
    fields = ("link_name", "link_path", "image", "notes")

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class LinkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Link
    fields = ("link_name", "link_path", "image", "notes")
    template_name = "links/link_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user_id == self.request.user


class LinkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Link
    template_name = "links/link_delete.html"
    success_url = reverse_lazy("link_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user_id == self.request.user
