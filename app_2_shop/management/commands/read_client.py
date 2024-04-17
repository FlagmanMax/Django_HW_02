from django.core.management.base import BaseCommand
from app_2_shop.models import Client

class Command(BaseCommand):
    help = "Get Client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        if client:
            self.stdout.write(f'Name: {client.name}; email: {client.email}')
        else:
            self.stdout.write(f'No client with this id')
