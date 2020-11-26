from django.shortcuts import render


context = {
    'title': 'Blogs',
}


def blogs_page(request):
    return render(request, 'blogs/blogs.html', context)
