from django.shortcuts import  render
from django.core.paginator import Paginator
from .models import Universities
from django.db.models import Q


def universities_page(request):

    title = 'Universities'

    search_query = request.GET.get('search', '')

    if search_query:
        data = Universities.objects.filter(
            Q(name__icontains=search_query) | Q(location__icontains=search_query)).distinct()
        title = f'Search results for {search_query}'
    else:
        data = Universities.objects.all()

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'universities': page_obj,
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'universities/universities.html', context)


def university_detail(request, slug):
    university = Universities.objects.get(slug=slug)

    return render(request, 'universities/university-detail.html', context={
        'title': university.name,
        'university': university
    })
