from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.http import request
from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from .models import Article
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ['title','body',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('articles')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


