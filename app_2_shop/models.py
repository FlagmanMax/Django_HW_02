from django.db import models

from django.utils import timezone
from datetime import date
from django.utils.translation import gettext as _

# Create your models here.

# Создайте три модели Django: клиент, товар и заказ. Клиент
# может иметь несколько заказов. Заказ может содержать
# несколько товаров. Товар может входить в несколько
# заказов.


# Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиента
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return f'{self.name} '


# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    item_date = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return f'{self.name} '


# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары,
# входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа
class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    item_id = models.ManyToManyField(Item)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return f'Order for client_id = {self.client_id} '

