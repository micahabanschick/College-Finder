from django.shortcuts import render
import time

t = time.localtime()
current_time = time.strftime("%I:%M %p", t)


context = {
    'title': 'Dashboard',
    'name': 'there',
    'current_time': current_time,
    'profile_completed': 0,
    'bookmarks_count': 0,
}


def dashboard_page(request):
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

    return render(request, 'dashboard/dashboard.html', context)
