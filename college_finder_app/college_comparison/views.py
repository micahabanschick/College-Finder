from django.shortcuts import render
from universities.models import Universities
from django.contrib import messages


universities = Universities.objects.all()

uni_names = []
for university in universities:
    uni_names.append(university.name)


context = {
    'title': 'College Comparison',
    'universities': universities,
    'uni_names': uni_names,
}


def college_comparison_page(request):
    # if 'term' in request.GET:
    #     qs = Universities.objects.filter(
    #         name__icontains=request.GET.get('term'))
    # messages.add_message(request, messages.SUCCESS,
    #                      'Logged in successfully.')
    return render(request, 'college_comparison/college_comparison.html', context)
