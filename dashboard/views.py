from django.shortcuts import render
import time
from universities.models import University

t = time.localtime()
current_time = time.strftime("%I:%M %p", t)

try:
    universities = University.objects.all()
    uni_bookmark_counts = []
    trending_unis = []
    for university in universities:
        num = university.bookmarks.count()
        uni_bookmark_counts.append(num)

    trending_unis_index = sorted(range(
        len(uni_bookmark_counts)), key=lambda i: uni_bookmark_counts[i], reverse=True)[:10]

    for index in trending_unis_index:
        trending_unis.extend(University.objects.filter(id=index))
except:
    pass


def dashboard_page(request):

    context = {
        'title': 'Dashboard',
        'name': 'there',
        'current_time': current_time,
        'profile_completed': 0,
        'bookmarks_count': 0,
    }

    name = request.user.get_short_name()
    if name != '':
        context['name'] = name.upper()

    profile_obj = request.user.profile
    null_count = 0
    for f in ["avatar", "bio", "gpa", "gre_score", "toefl_score", "lor_score", "research"]:
        if getattr(profile_obj, f, None) is None:
            null_count += 1
    context['profile_completed'] = int((10 - null_count) / 10 * 100)

    bookmarks_count = request.user.bookmarks.count()
    context['bookmarks_count'] = bookmarks_count

    context['trending_unis'] = trending_unis

    return render(request, 'dashboard/dashboard.html', context)
