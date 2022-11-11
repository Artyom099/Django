from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.

def index_page(request):

#     new_worker = Worker(name = 'Иват', surname = 'Закорюкин', salary = 70000)
#     new_worker.save()                   # сохраняем объект new_worker в БД

#     worker_to_change = Worker.objects.get(id = 5)       # достаем запись из БД
#     worker_to_change.surname = 'Задерищенский'          # меняем фамилию
#     worker_to_change.save()                             # записывем в БД
#     print(worker_to_change)

    all_workers = Worker.objects.all()
    print(all_workers)

#     workers_filtered = Worker.objects.filter(salary = 60_000)
#     print(workers_filtered)

    for i in all_workers:
            print(f'Фамилия: {i.surname}, Имя: {i.name}, Зарплта: {i.salary}, ID: {i.id}')

    return render(request, 'index.html', {'orders': Worker.objects.all()})
