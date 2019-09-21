from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

from . import models, forms


#  Show all Blogs
def blog_list(request):
    template = 'blog/blog_list.html'
    blogs = models.Blog.objects.filter(is_approved=True).order_by('-posted_date')
    context = {
        'blogs' :  blogs
        }
    return render(request, template, context=context)


# Show all data for admin
def admin_blog_list(request):
    template = 'blog/admin_blog_list.html'
    if not request.user.is_staff:
        messages.warning(request, 'You have no right to visit this page')
        return redirect('home')
    context = {
        'blogs':models.Blog.objects.all()}
    return render (request, template, context) 


def admin_blog_detail(request, pk):
    template = 'blog/admin_blog_detail.html'
    if not request.user.is_staff:
        messages.info(request, 'You have no right to visit this page')
        return redirect('home')
    context = {
        'blog':get_object_or_404(models.Blog, pk = pk)}
    return render(request, template, context)


def blog_detail(request, pk):
    template = 'blog/blog_detail.html'
    context = {
        'blog':get_object_or_404(models.Blog, pk = pk),
        'cmt_form': forms.comment_form }
    return render(request, template, context)


def write_blog_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in')
        return redirect ('login')

    if request.method == 'POST':
        form = forms.blog_form(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog = form.save()
            return HttpResponseRedirect (reverse ('blogs:blog_detail', kwargs={'pk':blog.id}))
    else:
        form = forms.blog_form()
        context = {
            'form':form,
            'state': 'Create'
            }
        return render(request, 'blog/blog_form.html', context)


def blog_update_view(request, pk):
    blog = get_object_or_404(models.Blog, pk=pk)
    user = request.user
    if not user.is_authenticated:
        messages.error(request, 'You have need to be logged in first')
        redirect('login')    
    if not user == blog.author:
        messages.error(request, 'You are not allowed to update this post')
        redirect('blogs:blog_list')
    if request.method == 'POST':
        form = forms.blog_form(request.POST or None, instance=blog)
        if form.is_valid():
            blog = form.save()
            return HttpResponseRedirect(blog.get_absolute_url())
    else:
        form = forms.blog_form(instance=blog)
    context = {
        'form':form,
        'state': 'Update'
        }
    return render(request, 'blog/blog_form.html', context)


def blog_delete(request, pk):
    blog = get_object_or_404(models.Blog, pk=pk)
    user = request.user
    if not user.is_authenticated:
        messages.error(request, 'You have to be logged in first')
        return redirect ('login')
    if not user.is_staff or not blog.author == user:
        messages.error(request, 'You cannot perform delete action on this form')
        return HttpResponseRedirect(reverse_lazy('blogs:blog_detail', kwargs={'pk':blog.id}))
    # elif not blog.author == user:
        # messages.error(request, 'You need to be admin.')
        # return HttpResponseRedirect(reverse_lazy('blogs:blog_detail', kwargs={'pk':blog.id}))
    else:
        blog.delete()
        messages.info(request, 'Blog has been deleted, successfully')
        return redirect('blogs:blog_list')
        context = {
            'blog': blog
        }
        return render(request, 'blog/blog_delete.html', context)


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
    comment = get_object_or_404(models.Comment, pk=pk)
    blog_pk = comment.blog.pk
    if comment.user == request.user or request.user.is_staff:
        comment.delete()
        messages.success(request, 'Comment Deleted')
    else:
        messages.error(request, 'You are not allowed to delete other peoples comment')
    return redirect('blogs:blog_detail', pk = blog_pk)


# Approve blog list
def blog_approval(request, pk):
    template = 'blog/admin_blog_list.html'
    blog = get_object_or_404(models.Blog, pk=pk)
    if not request.user.is_staff:
        messages.success(request, 'Only Staffs can perform the action')
    blog.approve(blog)
    admin_blog_list(request)
    context = {'blogs':models.Blog.objects.all().order_by('-is_approved')}
    return render (request, template, context) 

