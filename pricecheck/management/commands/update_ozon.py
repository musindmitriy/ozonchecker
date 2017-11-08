
from zipfile import ZipFile
import io

from lxml import etree
import requests

from django.core.management.base import BaseCommand

from pricecheck.models import Item, Price


class Command(BaseCommand):
    help = 'Запрашивает цены с ozon.ru'

    def handle(self, *args, **kwargs):

        url = 'http://static.ozone.ru/multimedia/feeds/facet/div_book/1140581.zip'
        file = io.BytesIO(requests.get(url).content)
        with ZipFile(file, 'r') as z:
            f = z.namelist()[0]
            xml = z.read(f)
        tree = etree.fromstring(xml)
        offers = tree.xpath("//offers")[0]
        for offer in offers:  # А в цикле не печатаем, как в предыдущей статье, а сохраняем в базе
            name = offer.find("name").text
            url = offer.find("url").text[:-len("?from=prt_xml_facet")]
            # Все ссылки заканчиваются на ?from=prt_xml_facet а нам это не нужно

            item, created = Item.objects.get_or_create(link=url, defaults={"name": name})
            # Создаём книгу, если она не существует
            # https://docs.djangoproject.com/en/stable/ref/models/querysets/#get-or-create

            price = float(offer.find("price").text)
            _, created = Price.objects.get_or_create(item=item, defaults={"price": price})
            # Создаём цену, если она ещё не была создана
