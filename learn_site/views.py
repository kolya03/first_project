from django.shortcuts import render
from scroll.models import ScrollSlider
from price.models import PriceCard, PriceTable

def first_page(request):
    scroll_list = ScrollSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()

    objs = {
        'scroll_list': scroll_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
    }
    return render(request, './index.html', objs)

