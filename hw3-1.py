def remains():
    from datetime import date
    seg = date.today() #какое число сегодня
    segg = seg.year + 1 #расчёт грядушего года
    newyear = date(segg, 1, 1) # 1 января следующего года
    ostalos = newyear - seg #расчёт разницы
    return ostalos.days #конверт даты в формат год-месяц-день

print('До Нового года осталось', remains(), 'дней')

