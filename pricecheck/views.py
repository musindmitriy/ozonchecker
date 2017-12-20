from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Item, Price


def list():
    pass


def main(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, "pricecheck/main.html", {"item": item})