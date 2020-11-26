from django.shortcuts import render


context = {
    'title': 'Universities',
}


def universities_page(request):
    return render(request, 'universities/universities.html', context)
