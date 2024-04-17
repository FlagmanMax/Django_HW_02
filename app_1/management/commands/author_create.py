from django.core.management.base import BaseCommand
from app_1.models import Author, Article

class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count authors')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1,count+1):
            author = Author(
                f_name=f'FirstName_{i}',
                l_name=f'LastName_{i}',
                email=f'mail_{i}@author.com',
            )
            author.save()

            for j in range (1, count+1):
                article = Article(
                    author=author,
                    title=f'Title_{j}',
                    content=f'Text from {author.f_name} # {j} Bla bla bla'
                )
                article.save()

        self.stdout.write('Hello world!')

