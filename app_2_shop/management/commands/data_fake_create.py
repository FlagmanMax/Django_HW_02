import random

from django.core.management.base import BaseCommand
from app_2_shop.models import Item, Client, Order


class Command(BaseCommand):
    help = "Generate test Items, Clients, Orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            item = Item(
                name=f'Item_{i}',
                description=f'Description for Item_{i}',
                price=i * 10,
                stock=i * 5
            )
            item.save()

            client = Client(
                name=f'Name_{i}',
                email=f'Name_{i}@mail.ru',
                phone=random.randint(89000000000, 89999999999),
                address=f'address_{i}'
            )
            client.save()

            total = item.price
            order = Order(
                client_id=client,
                total=total,
            )
            order.save()
            order.item_id.add(item.pk)
            order.save()
