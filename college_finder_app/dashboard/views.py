from django.shortcuts import render
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
greeting = "Hello"


context = {
    'title': 'Dashboard',
    'name': 'there',
    'current_time': current_time,
    'greeting': greeting,
}


def dashboard_page(request):
    name = request.user.get_short_name()
    if name != '':
        context['name'] = name.upper()
    return render(request, 'dashboard/dashboard.html', context)
