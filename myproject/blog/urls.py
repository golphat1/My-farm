from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    # URL pattern for the home page, using PostListView to display a list of posts
    path('', PostListView.as_view(), name='blog-home'),

    # URL pattern to display posts of a specific user, using UserPostListView
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    # URL pattern to display details of a specific post, using PostDetailView
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # URL pattern to create a new post, using PostCreateView
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # URL pattern to update an existing post, using PostUpdateView
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # URL pattern to delete an existing post, using PostDeleteView
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # URL pattern for the about page, using views.about function
    path('about/', views.about, name='blog-about'),
]
