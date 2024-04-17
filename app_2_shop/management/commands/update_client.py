from django.core.management.base import BaseCommand
from app_2_shop.models import Client


class Command(BaseCommand):
    help = "Update Client's name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')

        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.save()
        self.stdout.write(f'Updated name: {client.name}')