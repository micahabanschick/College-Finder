from django.shortcuts import render


context = {
    'title': 'Get Help',
}


def get_help_page(request):
    return render(request, 'get_help/get_help.html', context)
