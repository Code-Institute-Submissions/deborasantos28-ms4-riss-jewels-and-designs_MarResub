from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import BlogEntry
from .forms import CommentForm, BlogEntryForm


def blog_entry(request):
    """ A view to return the main blog page """
    posts = BlogEntry.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog_main.html', context)


def blog_detail(request, slug):
    """ A view that returns individual blog posts """
    blog_entry = get_object_or_404(BlogEntry, slug=slug)
    comments = blog_entry.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Creates new_comment object (doesn't save it)
            new_comment = comment_form.save(commit=False)
            # Assigns the value of what blogpost the user is on
            new_comment.post = blog_entry
            # Assigns the username (must be logged in to comment)
            new_comment.username = request.user
            new_comment.save()
            messages.info(request, 'Your message has been posted successfully!')
            return redirect(reverse('blog_descriptions', args=[blog_entry.slug]))
        else:
            messages.error(request, 'Failed to post your comment. Check that \
                the post is valid and try again.')
    else:
        comment_form = CommentForm()

    context = {
        'blog_entry': blog_entry,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_descriptions.html', context)


@login_required
def new_blog_post(request):
    """ A view to add blog posts to the blog """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Hop Shop Admin have \
            access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogEntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            new_post.save()
            messages.success(request, 'Your post has been posted successfully!')
            return redirect(reverse('blog_descriptions', args=[new_post.slug]))
        else:
            messages.error(request, 'Your post seems to have failed to be posted. Please check that \
                that all fields on the post are valid and try again.')
    else:
        form = BlogEntryForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/new_post.html', context)


@login_required
def edit_blog_post(request, slug):
    """ A view to edit existing blog posts in the blog """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only members of the Admin have \
            access to this page!')
        return redirect(reverse('home'))

    blog_entry = get_object_or_404(BlogEntry, slug=slug)

    if request.method == 'POST':
        form = BlogEntryForm(request.POST, request.FILES, instance=blog_entry)
        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.author = request.user
            edit_post.slug = slugify(edit_post.title)
            form.save()
            messages.success(request, 'Your blog post has been updated!')
            return redirect(reverse('blog_description', args=[edit_post.slug]))
        else:
            messages.error(request, 'Oh no! Your post failed to update. Check that \
                the post is valid and try again.')
    else:
        form = BlogEntryForm(instance=blog_entry)
        messages.info(request, f'You are currently editing the blog entry \
            "{blog_entry.title}"')

    context = {
        'form': form,
        'blog_entry': blog_entry,
    }

    return render(request, 'blog/edit_post_entry.html', context)


@login_required
def delete_blog_post(request, slug):
    """ A view that deletes a chosen blog post from the blog """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only members of the Admin have \
            access to this page!')
        return redirect(reverse('home'))

    blog_entry = get_object_or_404(BlogEntry, slug=slug)
    blog_entry.delete()
    messages.success(request, 'This entry has been deleted successfully!')
    return redirect(reverse('blog_main'))