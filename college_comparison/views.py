from django.shortcuts import render
from universities.models import University
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


unis_for_compare = []
uni_names_for_compare = []


@csrf_exempt
def college_comparison_page(request):

    universities = University.objects.all()

    uni_names = []
    for university in universities:
        uni_names.append(university.name)

    if request.method == 'POST':
        searched_uni = request.POST.get('searched_uni')
        if searched_uni in uni_names:
            valid_uni = searched_uni
            uni_obj = University.objects.filter(name=valid_uni)

            if ((len(unis_for_compare) < 3) and (valid_uni not in uni_names_for_compare)):
                uni_names_for_compare.append(valid_uni)
                unis_for_compare.extend(uni_obj)

    discard_uni = request.GET.get('discard_uni')
    if discard_uni:
        unis_for_compare.pop(int(discard_uni))

    context = {
        'title': 'College Comparison',
        'universities': universities,
        'uni_names': uni_names,
        'unis_for_compare': unis_for_compare,
    }

    return render(request, 'college_comparison/college_comparison.html', context)
