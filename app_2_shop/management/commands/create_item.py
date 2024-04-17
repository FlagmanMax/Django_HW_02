from django.core.management.base import BaseCommand
from app_2_shop.models import Item


class Command(BaseCommand):
    help = "Create item"


    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Clients name')
        parser.add_argument('description', type=str, help='description')
        parser.add_argument('price', type=float, help='price')
        parser.add_argument('stock', type=int, help='stock')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        stock = kwargs.get('stock')

        item = Item(
            name=name,
            description=description,
            price=price,
            stock=stock
        )

        item.save()
        self.stdout.write(f'Item {item} created')

