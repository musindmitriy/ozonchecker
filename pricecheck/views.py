import datetime, json
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Item, Price


def list():
    pass


def main(request, id):
    item = get_object_or_404(Item, pk=id)
    start_from = datetime.date.today() - datetime.timedelta(days=7)
    price_last = Price.objects.filter(item=item,
                                      date__gte=start_from).order_by("date")
    js = []
    for price in price_last:
        js.append(
            ['new Date("{}T00:00")'.format(price.date.isoformat()), price.price]
        )
    js = str(js).replace("'", "")
    return render(request, "pricecheck/main.html",
                  {"item": item, "price": js})