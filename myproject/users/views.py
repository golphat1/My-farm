from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.http import request
from .models import Post  # Import the Post model assuming it contains user posts
from django.contrib.auth import logout  # Import the logout function
from django.http import HttpResponseNotAllowed

def register(request):
    """
    View function for user registration.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """
    View function for user profile page.
    Allows users to update their profile information.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def user_posts(request):
    """
    View function for displaying posts created by the current user.
    """
    posts = Post.objects.filter(author=request.user)
    return render(request, 'users/posts.html', {'posts': posts})

@login_required
def custom_logout(request):
    """
    View function for custom logout.
    Logs the user out and redirects to the login page.
    """
    logout(request)  # This logs the user out
    # You can add additional functionality here
    return redirect('login')
