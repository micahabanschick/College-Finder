from django.http.response import HttpResponseRedirect
from universities.models import Universities
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


context = {
    'title': 'Bookmarks',
}


def bookmark(request, id):

    university = get_object_or_404(Universities, id=id)
    if university.bookmarks.filter(id=request.user.id).exists():
        university.bookmarks.remove(request.user)
        messages.add_message(
            request, messages.INFO, f'{university.name} removed from your bookmark.')
    else:
        university.bookmarks.add(request.user)
        messages.add_message(
            request, messages.SUCCESS, f'{university.name} added to your bookmark.')

    return redirect('universities') #THIS LINE !!!



def bookmarks_page(request):
    return render(request, 'bookmarks/bookmarks.html', context)
