from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


from .models import Link, Tag
from .forms import CustomEditLinkForm

# Create your views here.


class LinkListView(LoginRequiredMixin, ListView):
    model = Link
    context_object_name = "link_list"
    template_name = "links/craftbox.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()

        ctx["tags"] = Tag.objects.filter(user=self.request.user)
        return ctx


class LinkDetailView(LoginRequiredMixin, DetailView):
    model = Link
    template_name = "links/link_detail.html"


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    template_name = "links/link_new.html"
    fields = ("link_name", "link_path", "image", "notes", "tags")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LinkUpdateView(LoginRequiredMixin, UpdateView):
    model = Link
    form_class = CustomEditLinkForm
    success_url = reverse_lazy("link_list")
    template_name = "links/link_edit.html"


class LinkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Link
    template_name = "links/link_delete.html"
    success_url = reverse_lazy("link_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/tag_create.html"
    fields = ("tag_name",)
    success_url = reverse_lazy("link_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TagUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    fields = ("tag_name",)
    template_name = "tags/tag_edit.html"
    success_url = reverse_lazy("link_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class TagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tag
    template_name = "tags/tag_delete.html"
    success_url = reverse_lazy("link_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
