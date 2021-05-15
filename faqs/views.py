from django.shortcuts import render


context = {
    'title': 'FAQs',
}


def faqs_page(request):
    return render(request, 'faqs/faqs.html', context)
