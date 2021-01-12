from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Universities

data = Universities.objects.all()


def universities_page(request):
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Universities',
        'universities': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'universities/universities.html', context)


def university_detail(request, slug):
    university = Universities.objects.get(slug=slug)

    return render(request, 'universities/university-detail.html', context={
        'title': university.name,
        'university': university
    })
