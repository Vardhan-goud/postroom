from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator


class AboutView(TemplateView):
    template_name="blog/about.html"


class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    ordering=['-date_posted']
    context_object_name='posts'
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(tag=self.kwargs['tag']).order_by('-date_posted')


class PostDetailView(DetailView):
    model=Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','tag']
    def form_valid(self,form):
        form.instance.author=self.request.user 
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','tag']
    def form_valid(self,form):
        form.instance.author=self.request.user 
        return super().form_valid(form)
    def test_func(self) :
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else :
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
      model=Post
      success_url='/'
      def test_func(self) :
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else :
            return False

def searchByUser(request):
    query = request.GET.get('searchUser')
    posts = Post.objects.filter(author__username__icontains=query).order_by('-date_posted')
    if posts:
        return render(request,'blog/search_user.html',{'posts':posts,'query':query})
    else:
        return render(request,'blog/no_search_results.html',{'query':query})

def searchByTag(request):
    query = request.GET.get('searchTag')
    posts = Post.objects.filter(tag__icontains=query).order_by('-date_posted')
    if posts:
        return render(request,'blog/search_tag.html',{'posts':posts,'query':query})
    else:
        return render(request,'blog/no_search_results.html',{'query':query})