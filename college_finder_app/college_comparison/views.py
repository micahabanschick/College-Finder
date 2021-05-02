from django.shortcuts import render
from universities.models import Universities
from django.contrib import messages


universities = Universities.objects.all()

uni_names = []
for university in universities:
    uni_names.append(university.name)

def college_comparison_page(request):
    # unis_list_to_compare = request.POST.getlist('unisForCompare')
    # cc = request.POST.getlist('unisForCompare')
    # print(cc)
    context = {
        'title': 'College Comparison',
        'universities': universities,
        'uni_names': uni_names,
        # 'unis_list_to_compare': unis_list_to_compare,
        # 'cc': cc,
    }

    return render(request, 'college_comparison/college_comparison.html', context)
