from django.shortcuts import render
from django.views import generic

from . import models, forms


class ArticleListView(generic.ListView):
    model = models.Article
    # template_name = 'blog/index.html'
    ordering = ['-posted_date']


class BlogDetailView(generic.DetailView):
    model = models.Article

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['form'] = forms.comment_form
        return context



class ArticleCreateView(generic.CreateView):
    fields = ('title', 'content')
    model = models.Article

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(generic.UpdateView):
    pass

class ArticleDeteleView(generic.DeleteView):
    pass


def article_comment(request):
    pass