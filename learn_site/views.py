from django.shortcuts import render
from scroll.models import ScrollSlider
from price.models import PriceCard, PriceTable
from crm.models import Order
from telebot.sendmessage import sendTelegram

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

def last_page(request):
    name = request.POST['or_name']
    phone = request.POST['or_phone']
    ob = Order(order_name=name, order_phone=phone)
    ob.save()
    sendTelegram(tg_name=name, tg_phone = phone)
    return render(request, './last_page.html', {
        'name': name,
    })

