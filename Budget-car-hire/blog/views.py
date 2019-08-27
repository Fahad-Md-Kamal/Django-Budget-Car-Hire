from django.shortcuts import render
from django.views import generic

from . import models


class ArticleListView(generic.ListView):
    model = models.Article
    template_name = 'blog/index.html'


class ArticleDetailView(generic.DetailView):
    model = models.Article


class ArticleCreateView(generic.CreateView):
    fields = ('title', 'content')
    model = models.Article

class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass

class ArticleDeteleView(generic.DeleteView):
    pass