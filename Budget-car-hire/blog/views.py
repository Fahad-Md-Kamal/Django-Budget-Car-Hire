from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from . import models, forms


class ArticleListView( generic.ListView):
    template_name = 'blog/article_list.html'
    model = models.Article
    queryset = models.Article.objects.all()
    ordering = ['-posted_date']


class AdminArticleView(LoginRequiredMixin,  generic.ListView, ):

    template_name = 'blog/admin_blog_list.html'
    model = models.Article
    queryset = models.Article.objects.all()
    context_object_name = 'blogs'
    ordering = ['-posted_date']
    

class AdminArticleDetail(generic.DetailView):
    template_name = 'blog/admin_blog_detail.html'
    model = models.Article
    context_object_name = 'article'


class ArticleDetailView(generic.DetailView):
    model = models.Article

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Article, id=_id)

    ## Adding additional data to the context data dictionary
    def get_context_data(self,  *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = forms.comment_form
        return context


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'blog/article_form.html'
    login_url = 'login'
    form_class = forms.article_form
    success_message = "New article created"

    ## adds user's info with the data
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)



class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = 'blog/article_form.html'
    form_class = forms.article_form
    success_message = "Article Updated"
    permission_denied_message = 'You don\'t have the permission'
    

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Article, id=_id)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class ArticleDeteleView(LoginRequiredMixin, generic.DeleteView):
    model = models.Article
    success_url = reverse_lazy ('blogs:blog_list')


@login_required
def create_comment(request, pk):
    article = get_object_or_404(models.Article, pk = pk)
    user = request.user
    if request.method == 'POST':
        form = forms.comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = user
            comment.save()
            messages.success(request, f'Comment added for - {article.title} ')
            return redirect('blogs:blog_detail', pk = article.pk)

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(models.Comment, pk = pk)
    article_pk = comment.article.pk
    if comment.user == request.user or request.user.is_staff:
        comment.delete()
        messages.success(request, 'Comment Deleted')
    else:
        messages.error(request, 'You are not allowed to delete other peoples comment')

    return redirect('blogs:blog_detail', pk = article_pk)

