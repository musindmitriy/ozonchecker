import datetime
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import Item, Price


def list(request, page=1):
    items = Item.objects.all()
    paginator = Paginator(items, 25)
    items = paginator.get_page(page)
    return render(request, "pricecheck/list.html", {"items": items})


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
