from django.shortcuts import render


context = {
    'title': 'Dashboard',
}


def dashboard_page(request):
    return render(request, 'dashboard/dashboard.html', context)
