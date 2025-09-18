print('Давайте узнаем ваши инициалы')
fio = input('ФИО:')
name = fio.split()
ini = name[0][:1] + name[1][:1] + '.' + name[2][:1] + '.'
print(ini)
print(len(fio.replace(' ', '')))
