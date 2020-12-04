from django.shortcuts import render
from django.contrib.auth.decorators import login_required


context = {
    'title': 'Dashboard',
}


@login_required
def dashboard_page(request):
    return render(request, 'dashboard/dashboard.html', context)
