from django.shortcuts import render


context = {
    'title': 'College Comparison',
}


def college_comparison_page(request):
    return render(request, 'college_comparison/college_comparison.html', context)
