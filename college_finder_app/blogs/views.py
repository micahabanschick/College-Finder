from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.template.defaultfilters import slugify
from .forms import PostForm
from taggit.models import Tag


def blogs_page(request):

    title = 'Blogs'

    search_query = request.GET.get('search', '')

    if search_query:
        data = Post.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)).distinct()
        title = f'Search results for {search_query}'
    else:
        data = Post.objects.order_by('-posted_on')

    paginator = Paginator(data, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'blogs': page_obj,
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'blogs/blogs.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    previous_post = post.get_previous_by_posted_on
    next_post = post.get_next_by_posted_on

    return render(request, 'blogs/blog-detail.html', context={
        'title': post.title,
        'blog': post,
        'previous_post': previous_post,
        'next_post': next_post,
    })


def create_post(request):
    # Show most common tags
    common_tags = Post.tags.most_common()[:3]
    if request.method == 'POST':
        print(request.POST)
        blog_form = PostForm(request.POST)
        if blog_form.is_valid():
            newpost = blog_form.save(commit=False)
            newpost.slug = slugify(newpost.title)
            newpost.author = request.user
            newpost.save()
            # Without this next line the tags won't be saved.
            blog_form.save_m2m()
            messages.success(request, 'Successfully Posted!')
            return redirect('blogs')
        else:
            messages.info(
                request, f'Could not post, {blog_form.errors}')

    else:
        blog_form = PostForm()

    return render(request, 'blogs/create-post.html', {
        'blog_form': blog_form,
        'common_tags': common_tags,
        'title': 'Create Post'
    })


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    posts = Post.objects.filter(tags=tag)
    title = f'Articles tagged under "{tag}"'
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'blogs': page_obj,
        'page_obj': page_obj,
        'tagged': True,
        'tag': tag,
    }
    return render(request, 'blogs/blogs.html', context)
