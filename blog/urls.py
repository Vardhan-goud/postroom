from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,TagPostListView,search_tag,search_user

urlpatterns = [
    path('',PostListView.as_view(), name="home" ),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('tag/<str:tag>', TagPostListView.as_view(), name='tag-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name="post-update"),
    path('search_tag/', search_tag, name='search-tag'),
    path('search_user/', search_user, name='search-user'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name="post-delete")
]