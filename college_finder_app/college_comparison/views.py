from django.shortcuts import render
from universities.models import Universities
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


universities = Universities.objects.all()

uni_names = []
for university in universities:
    uni_names.append(university.name)
unis_for_compare = []


@csrf_exempt
def college_comparison_page(request):
    if request.method == 'POST':
        searched_uni = request.POST.get('searched_uni')
        if searched_uni in uni_names:
            valid_uni = searched_uni

            if ((len(unis_for_compare) < 3) and (valid_uni not in unis_for_compare)):
                uni_obj = Universities.objects.filter(name=valid_uni)
                unis_for_compare.extend(uni_obj)

        else:
            messages.add_message(request, messages.WARNING,
                                 'University Not Found.')

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
