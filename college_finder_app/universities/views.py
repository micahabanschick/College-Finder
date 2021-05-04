from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Universities
from django.db.models import Q
import ast

universities = Universities.objects.all()
uni_names = []
for university in universities:
    uni_names.append(university.name)


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
        'bookmarked_unis': bookmarked_unis,
        'data': data,
        'uni_names': uni_names,
    }
    return render(request, 'universities/universities.html', context)


def university_detail(request, slug):
    university = Universities.objects.get(slug=slug)
    labels = ['Teaching', 'Research',
              'Citations', 'Industry Income', 'International Outlook']
    data = [float(university.scores_teaching),
            float(university.scores_research), float(university.scores_citations), float(university.scores_industry_income), float(university.scores_international_outlook)]
    info = zip(labels, data)

    intl_stds = int(university.stats_pc_intl_students.replace("%", ""))
    local_stds = 100-intl_stds
    female_stds = university.stats_female_male_ratio.split(':')[0]
    male_stds = university.stats_female_male_ratio.split(':')[1]
    subjects = university.subjects_offered
    subject_list = ast.literal_eval(subjects)
    subjects_count = len(subject_list)
    col1, col2, col3 = [], [], []
    for subject in range(subjects_count):
        if subject % 3 == 0:
            col1.append(subject_list[subject])
        if subject % 3 == 1:
            col2.append(subject_list[subject])
        if subject % 3 == 2:
            col3.append(subject_list[subject])

    prev_uni = Universities.objects.filter(
        id__lt=university.id).order_by('rank_order').last()
    next_uni = Universities.objects.filter(
        id__gt=university.id).order_by('rank_order').first()

    uni_overall_score = university.scores_overall
    uni_overall_score_temp = uni_overall_score.split("–")[0]

    chance_of_admit_pct = request.user.profile.chance_of_admit * 100
    chance_texts = ['very high', 'high', 'good',
                    'low', 'very low', 'no']

    if chance_of_admit_pct != 0:
        chance = float(chance_of_admit_pct) - float(uni_overall_score_temp)

        if chance >= 30:
            chance_text = chance_texts[0]
        if chance < 30 and chance >= 20:
            chance_text = chance_texts[1]
        if chance < 20 and chance >= 5:
            chance_text = chance_texts[2]
        if chance < 5 and chance >= 0:
            chance_text = chance_texts[3]
        if chance < 0 and chance >= -20:
            chance_text = chance_texts[4]
        if chance < -20:
            chance_text = chance_texts[5]

        predict_result = f'You have {chance_text.upper()} chance of getting admission on this university.'
    else:
        predict_result = 'You must have 100% profile completion in order to predict chances.'

    return render(request, 'universities/university-detail.html', context={
        'title': university.name,
        'university': university,
        'labels': labels,
        'data': data,
        'info': info,
        'intl_stds': intl_stds,
        'local_stds': local_stds,
        'female_stds': female_stds,
        'male_stds': male_stds,
        'subjects': subject_list,
        'prev_uni': prev_uni,
        'next_uni': next_uni,
        'col1': col1, 'col2': col2, 'col3': col3,
        'predict_result': predict_result,
    })
