from django.shortcuts import render
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
    page_int = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_int)
    bookmarked_unis = request.user.bookmarks.all()

    context = {
        'title': title,
        'universities': page_obj,
        'page_obj': page_obj,
        'search_query': search_query,
        'bookmarked_unis': bookmarked_unis
    }
    return render(request, 'universities/universities.html', context)


def university_detail(request, slug):
    university = Universities.objects.get(slug=slug)
    labels = ['Teaching', 'Research',
              'Citations', 'Industry Income', 'International Outlook']
    data = [float(university.scores_teaching),
            float(university.scores_research), float(university.scores_citations), float(university.scores_industry_income), float(university.scores_international_outlook)]
    info = zip(labels, data)

    intl_stds = university.stats_pc_intl_students.replace("%", "")
    subjects = university.subjects_offered

    return render(request, 'universities/university-detail.html', context={
        'title': university.name,
        'university': university,
        'labels': labels,
        'data': data,
        'info': info,
        'subjects': subjects,
        'intl_stds': int(intl_stds),
    })
