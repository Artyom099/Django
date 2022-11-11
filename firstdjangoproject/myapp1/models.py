from django.db import models

# Create your models here.

class Worker(models.Model):                                     # название таблицы
    name = models.CharField(max_length=128, blank = False)     # столбцы таблицы с описанием типа данных
    surname = models.CharField(max_length=128, blank = False)
    salary = models.IntegerField(default = 0)

    def __str__(self):                  # этот метод отобржет имя пользователя в таблице (названии объекта)
        return f'{self.surname} {self.name}'
