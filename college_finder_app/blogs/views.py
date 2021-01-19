from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q

# from django.template.defaultfilters import slugify
# from .forms import PostForm
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

    return render(request, 'blogs/blog-detail.html', context={
        'title': post.title,
        'blog': post,
    })


# def blogs_page(request):
#     posts = Post.objects.order_by('-published')
#     # Show most common tags 
#     common_tags = Post.tags.most_common()[:4]
#     form = PostForm(request.POST)
#     if form.is_valid():
#         newpost = form.save(commit=False)
#         newpost.slug = slugify(newpost.title)
#         newpost.save()
#         # Without this next line the tags won't be saved.
#         form.save_m2m()
#     context = {
#         'posts':posts,
#         'common_tags':common_tags,
#         'form':form,
#     }
#     return render(request, 'blogs/blogs.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    title = f'Search results for {tag}' 
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'blogs': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'blogs/blogs.html', context)
