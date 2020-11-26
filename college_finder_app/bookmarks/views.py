from django.shortcuts import render


context = {
    'title': 'Bookmarks',
}


def bookmarks_page(request):
    return render(request, 'bookmarks/bookmarks.html', context)
