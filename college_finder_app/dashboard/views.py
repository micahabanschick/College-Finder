from django.shortcuts import render
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
greeting = "Hello"
emoji = "👋"

if int(time.strftime("%H", t)) < 4 and int(time.strftime("%H", t)) < 12:
    greeting = "Good Morning"
    emoji = "🌅"

if int(time.strftime("%H", t)) >= 12 and int(time.strftime("%H", t)) < 17:
    greeting = "Good Afternoon"
    emoji = "🌞"

if int(time.strftime("%H", t)) >= 17 and int(time.strftime("%H", t)) < 21:
    greeting = "Good Evening"
    emoji = "🌇"

if int(time.strftime("%H", t)) >= 21 and int(time.strftime("%H", t)) < 24:
    emoji = "🌃"


context = {
    'title': 'Dashboard',
    'name': 'there',
    'current_time': current_time,
    'greeting': {'text': greeting, 'emoji': emoji},
}


def dashboard_page(request):
    name = request.user.get_short_name()
    if name != '':
        context['name'] = name.upper()
    return render(request, 'dashboard/dashboard.html', context)
