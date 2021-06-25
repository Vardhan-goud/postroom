from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(), name="home" ),
    path('about/',views.AboutView.as_view(), name="about" ),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('tag/<str:tag>', views.TagPostListView.as_view(), name='tag-posts'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
    path('post/new/',views.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name="post-update"),
    path('search_tag/', views.searchByTag, name='search-tag'),
    path('search_user/', views.searchByUser, name='search-user'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name="post-delete"),
]