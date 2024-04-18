from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

def home(request):
    """
    View function for the home page.

    Retrieves all posts from the database and renders them on the home page.

    Args:
        request: HTTP request object.

    Returns:
        Rendered response containing the home page template with the retrieved posts.
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    """
    View class for displaying a list of posts.

    Attributes:
        model: The model to query for the list of posts (Post).
        template_name: The template used to render the list view.
        context_object_name: The variable name used in the template to access the list of posts.
        ordering: The ordering of the posts by the date posted, newest first.
        paginate_by: The number of posts to display per page, paginated by 5.
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    """
    View class for displaying a list of posts by a specific user.

    Attributes:
        model: The model to query for the list of posts (Post).
        template_name: The template used to render the list view.
        context_object_name: The variable name used in the template to access the list of posts.
        paginate_by: The number of posts to display per page, paginated by 5.
    """
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """
        Retrieves the list of posts authored by a specific user.

        Returns:
            QuerySet of posts authored by the specified user, ordered by date posted (newest first).
        """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    """
    View class for displaying the details of a single post.

    Attributes:
        model: The model to query for the post details (Post).
    """
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View class for creating a new post.

    Attributes:
        model: The model to use for creating the new post (Post).
        fields: The fields from the model to include in the form (title, content).
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        Sets the author of the post to the current user.

        Args:
            form: The form representing the new post.

        Returns:
            Super call to form_valid method to save the form.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View class for updating an existing post.

    Attributes:
        model: The model to use for updating the post (Post).
        fields: The fields from the model to include in the form (title, content).
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        Sets the author of the post to the current user.

        Args:
            form: The form representing the updated post.

        Returns:
            Super call to form_valid method to save the form.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Checks if the current user is the author of the post.

        Returns:
            True if the current user is the author of the post, False otherwise.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View class for deleting an existing post.

    Attributes:
        model: The model to use for deleting the post (Post).
        success_url: The URL to redirect to after successful deletion (/).
    """
    model = Post
    success_url = '/'

    def test_func(self):
        """
        Checks if the current user is the author of the post.

        Returns:
            True if the current user is the author of the post, False otherwise.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    """
    View function for the about page.

    Args:
        request: HTTP request object.

    Returns:
        Rendered response containing the about page template.
    """
    return render(request, 'blog/about.html', {'title': 'About'})