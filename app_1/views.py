# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или
# решка.
# Также запоминайте время броска
#
# Задание №2
# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.



import random

from django.shortcuts import render
from random import randint, choice

import logging
from django.http import HttpResponse
from django.utils import timezone
from . import models
from .models import HeadsTails
from .models import Article, Author

logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, filename="logger.log", filemode='a', format='%(levelname),s %(message)s')
# Create your views here.


def seminar2(request):
    logger.info(f'{request} request received!')

    test = """
    <head>Семинар 2</head>
    <body>
        <br><a href="http://127.0.0.1:8000/seminar2/heads_tails">Орел и Решка</a>
        <br><a href="http://127.0.0.1:8000/seminar2/statistic">Статистика за последние 5</a>
    </body>
    """

    return HttpResponse(test)


def heads_tails(request):
    logger.info(f'heads_tails!')
    res = random.choice(['Орел', 'Решка'])

    res_w = HeadsTails(res=res)
    res_w.save()

    return HttpResponse(res)


def statistic(request):
    logger.info(f'{request} request received!')
    n = request.GET.get('n', '5')
    data = HeadsTails.statistic(int(n))

    return HttpResponse(f"{data}")


def authors_read(request):
    logger.info(f'{request} request received!')
    authors = Author.objects.all()
    return HttpResponse(authors)

def articles_read(request):
    logger.info(f'{request} request received!')
    articles = Article.objects.all()
    return HttpResponse(articles)

def articles_by_author(request):
    logger.info(f'{request} request received!')
    name = request.GET.get('name')
    author_id = Author.objects.filter(f_name=name).first()
    articles = Article.objects.filter(author=author_id).all()
    return HttpResponse(articles)

