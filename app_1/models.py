# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или решка.
# Также запоминайте время броска
#
# Задание №2
# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.

from django.db import models
from django.utils import timezone
from datetime import date
from django.utils.translation import gettext as _

# Create your models here.


class HeadsTails(models.Model):
    rest_time = models.DateTimeField(default=timezone.now)
    res = models.CharField(max_length=50)

    # def __init__(self, rest_time, res):
    #     self.rest_time = rest_time
    #     self.res = res

    @staticmethod
    def statistic(n):
        dict_res = {"Орел": 0, "Решка": 0}
        query = list(HeadsTails.objects.all())
        if n > len(query):
            n = len(query)
        list_res = query[-n:]
        for item in list_res:
            if item.res == "Орел":
                dict_res['Орел'] += 1
            elif item.res == "Решка":
                dict_res['Решка'] += 1
        return dict_res

    def __str__(self):
        return f" time: {self.rest_time}, res: {self.res}"

# Создайте модель Автор. Модель должна содержать
# следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное
# имя”, которое возвращает имя и фамилию.

class Author(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField(_("Date"), default=date.today)

    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    def __str__(self):
        return f'{self.full_name()}'

# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию
# False


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(_("Date"), default=date.today)
    category = models.CharField(max_length=100)
    show_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} '