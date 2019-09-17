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


class BlogListView( generic.ListView):
    template_name = 'blog/blog_list.html'
    model = models.Blog
    queryset = models.Blog.objects.all()
    ordering = ['-posted_date']


# class AdminblogView(LoginRequiredMixin,  generic.ListView, ):

#     template_name = 'blog/admin_blog_list.html'
#     model = models.blog
#     queryset = models.blog.objects.all()
#     context_object_name = 'blogs'
#     ordering = ['-posted_date']


def admin_blog_list(request):
    if not request.user.is_staff:
        messages.warning(request, 'You have no right to visit this page')
        return redirect('home')

    return render (request, 'blog/admin_blog_list.html', {'blogs':models.blog.objects.all()}) 

    

# class AdminblogDetail(generic.DetailView):
#     template_name = 'blog/admin_blog_detail.html'
#     model = models.blog
#     context_object_name = 'blog'


def admin_blog_detail(request, pk):
    if not request.user.is_staff:
        messages.info(request, 'You have no right to visit this page')
        return redirect('home')

    template = 'blog/admin_blog_detail.html'
    context = {
        'blog':get_object_or_404(models.blog, pk = pk), 
        'msg': 'Working Fine'}
    return render(request, template, context)



# class blogDetailView(generic.DetailView):
#     model = models.blog

#     def get_object(self):
#         _id = self.kwargs.get("pk")
#         return get_object_or_404(models.blog, id=_id)

#     ## Adding additional data to the context data dictionary
#     def get_context_data(self,  *args, **kwargs):
#         context = super(blogDetailView, self).get_context_data(**kwargs)
#         context['form'] = forms.comment_form
#         return context



def blog_detail(request, pk):
    template = 'blog/blog_detail.html'







class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'blog/blog_form.html'
    login_url = 'login'
    form_class = forms.blog_form
    success_message = "New blog created"

    ## adds user's info with the data
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(blogCreateView, self).form_valid(form)



class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = 'blog/blog_form.html'
    form_class = forms.blog_form
    success_message = "blog Updated"
    permission_denied_message = 'You don\'t have the permission'
    

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Blog, id=_id)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class BlogDeteleView(LoginRequiredMixin, generic.DeleteView):
    model = models.Blog
    success_url = reverse_lazy ('blogs:blog_list')


@login_required
def create_comment(request, pk):
    blog = get_object_or_404(models.Blog, pk = pk)
    user = request.user
    if request.method == 'POST':
        form = forms.comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = user
            comment.save()
            messages.success(request, f'Comment added for - {blog.title} ')
            return redirect('blogs:blog_detail', pk = blog.pk)

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(models.Comment, pk = pk)
    blog_pk = comment.blog.pk
    if comment.user == request.user or request.user.is_staff:
        comment.delete()
        messages.success(request, 'Comment Deleted')
    else:
        messages.error(request, 'You are not allowed to delete other peoples comment')

    return redirect('blogs:blog_detail', pk = blog_pk)

