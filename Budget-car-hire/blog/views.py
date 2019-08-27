from django.shortcuts import render
from django.views import generic

from . import models


class ArticleListView(generic.ListView):
    model = models.Article
    # template_name = 'blog/index.html'
    # context_object_name = 'articles'  ## generally the data is send as object_list
    ordering = ['-posted_date']


class ArticleDetailView(generic.DetailView):
    model = models.Article


class ArticleCreateView(generic.CreateView):
    fields = ('title', 'content')
    model = models.Article

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass

class ArticleDeteleView(generic.DeleteView):
    pass