from django.contrib import admin
from .models import Worker          # импортировать модель из файла тоже надо!

# Register your models here.
# здесь регистрируются модели из фйла models, чтобы они обновлялись в интерфейсе администратора

admin.site.register(Worker)
