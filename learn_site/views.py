from django.shortcuts import render
from scroll.models import ScrollSlider

def first_page(request):
    scroll_list = ScrollSlider.objects.all()
    return render(request, './index.html', {
        'scroll_list': scroll_list
    })

