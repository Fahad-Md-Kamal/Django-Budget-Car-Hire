from django.shortcuts import render
from django.views import generic

from . import models, forms


class ArticleListView(generic.ListView):
    model = models.Article
    # template_name = 'blog/index.html'
    ordering = ['-posted_date']


class BlogDetailView(generic.DetailView):
    model = models.Article


    def get_context_data(self,  *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['form'] = forms.comment_form
        return context

# def BlogDetailView(request, pk):
#     if request.method == "POST":
#         data = { 'user' : request.user.username,
#                     'article_id': pk
#                 }
#         form = forms.comment_form()

# form = CreateASomething(request.POST)
# if form.is_valid():
#     obj = form.save(commit=False)
#     obj.field1 = request.user
#     obj.save()



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