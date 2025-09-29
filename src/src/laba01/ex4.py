print('Добро пожаловать в переводчик минут.')
print('Данный код переводит минуты в формат ЧЧ:ММ.')
minutes = int(input("Введите кол-во минут: "))
hours = minutes // 60
mins = minutes % 60
print(f'Результат перевода: {hours}:{mins}')