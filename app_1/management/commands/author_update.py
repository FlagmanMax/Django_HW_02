from django.core.management.base import BaseCommand
from app_1.models import Author, Article

class Command(BaseCommand):
    help = "Update Author by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Primary key')
        parser.add_argument('email', type=str, help='Email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        author.email = kwargs.get('email')
        author.save()
        self.stdout.write(f'Author.email: {author.email}')