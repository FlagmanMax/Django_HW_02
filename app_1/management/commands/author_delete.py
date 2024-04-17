from django.core.management.base import BaseCommand
from app_1.models import Author, Article

class Command(BaseCommand):
    help = "Delete Author by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Primary key')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        author.delete()
        self.stdout.write(f'Author: {author}')