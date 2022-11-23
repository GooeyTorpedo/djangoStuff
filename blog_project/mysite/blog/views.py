from time import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, 
DetailView, CreateView, UpdateView, DeleteView)
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'    
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'    
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')

#################################
#################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish
    return redirect('post_detail', pk=pk)


@login_required #make view below reuired to be logged in first
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk) #pass in Post model to get primary key, if cant find it, return 404 page
    if request.method == 'POST': # 'POST' means someone filled in form and submit it
        form = CommentForm(request.POST)
        if form.is_valid(): #if nothing wrong with form submitted
            comment = form.save(commit = False)
            comment.post = post #in models.py, the comment model have attribute of post, connected by foreign key #make the post in comment model the post itself
            comment.save()
            return redirect('post_detail', pk= post.pk)

    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk) #pass in Comment model to get primary key, if cant find it, return 404 page
    comment.approve() #model Comment have approve method
    return redirect('post_detail', pk=comment.post.pk) #Comment model have property 'post'. Now we redirect ourself to the post of this particular comment

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)