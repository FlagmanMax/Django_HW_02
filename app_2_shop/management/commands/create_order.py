from django.core.management.base import BaseCommand
from app_2_shop.models import Item, Client, Order


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client id')
        parser.add_argument('item_id', type=int, help='item_id')


    def handle(self, *args, **kwargs):
        item_id = kwargs.get('item_id')
        item = Item.objects.filter(pk=item_id).first()

        client_id = kwargs.get('client_id')
        client = Client.objects.filter(pk=client_id).first()

        order = Order.objects.filter(client_id=client_id).first()

        if not order:
            total = item.price
            order = Order(
                client_id=client,
                total=total,
            )
            order.save()

            order.item_id.add(item.pk)
            order.save()

            self.stdout.write(f'Order {order} created')
        else:
            total = order.total + item.price

            order = Order(
                client_id=client,
                total=total,
            )
            order.save()

            order.item_id.add(item.pk)
            order.save()

            self.stdout.write(f'Order {order} updated')


