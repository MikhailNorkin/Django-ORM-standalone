import os
import django
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit
from django.utils import timezone
from math import floor


# Функция возвращает True при визите более 23 часов
def  is_visit_long (visit , min = 60 ):
    hour_second_23 = min * 60 * 23
    if (visit.leaved_at - visit.entered_at).total_seconds() > hour_second_23: 
        return True    
    return  False

# Функция переводит секунды в часы, минуты и секунды
def format_time(seconds):
    hours = floor(seconds // 3600)
    mins = floor((seconds-hours*3600) // 60)
    secs = floor(seconds - hours * 3600 - mins * 60)
    return '{}:{:02}:{:02}'.format(hours, mins, secs)

if __name__ == '__main__':
    visits = Visit.objects.all()
    print(visits)
    print()

    # Задание 8. Получение завершенных визитов пользователей
    visit_in = Visit.objects.filter(leaved_at = None)
    print(visit_in)
    print()
    # Задание8. Конец
    
    # Задание 9. Кто сейчас находится в хранилище
    for visit in visit_in:
        time_in = timezone.localtime(visit.entered_at, pytz.timezone('Europe/Moscow'))
        print('Зашел в хранилище по Москве\n' + str(time_in.strftime("%Y-%m-%d %H:%M:%S")) +'\n')

        # Задание 10. Сколько времени посетители провели в хранилище
        delta = timezone.localtime() - visit.entered_at
        seconds = delta.total_seconds()
        print('Находится в хранилище\n' + str(format_time(seconds)))
        # Задание 10. Конец

    print()
    # Задание 9. Конец

    for visit in visit_in:
        print(str(visit.passcard.owner_name))
    print

    #Задание 13. Получить визиты по пропуску:
    passcard_pass_ziro = visits[0].passcard
    pass_s = Visit.objects.filter(passcard = passcard_pass_ziro)
    print(pass_s)
    print()
    #Задание 13. Конец

    # Задание 14. Проверка визитов на подозрительность (Сделал больше 23 часов):
    print("Визиты дольше 23 часов")
    visits_not_end = Visit.objects.filter(leaved_at__isnull = False)
    for visit_attention in visits_not_end:
        if is_visit_long(visit_attention, 60) == True:
            print(visit_attention)
    # Задание 14. Конец
    
