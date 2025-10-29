## Лабораторная работа 5
### Задание A — JSON ↔ CSV
```python
import csv, json, sys, os

def is_valid_json_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
        
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)  # Загружаем и переводим JSON данные из файла
            return isinstance(json_data, list) and len(json_data) > 0 and all(isinstance(item, dict) for item in json_data) #все элементы в списке являются словарями
    except:
        return False

def is_valid_csv_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
            
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  # Создаем объект reader для чтения CSV файла построчно
            header = next(reader, None) # Читаем первую строку (заголовок) из CSV файла
            return header is not None and len(header) > 0
    except:
        return False

def json_to_csv(json_path: str, csv_path: str) -> None:
    if not is_valid_json_file(json_path): # Проверяем валидность CSV файла с помощью нашей функции
        print("ValueError: Input file is not a valid JSON or is empty")
        sys.exit(1) # Завершаем программу с кодом ошибки 1

    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file) # Загружаем и парсим JSON данные в переменную json_data

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys()) # Создаем объект DictWriter для записи словарей в CSV
        writer.writeheader()  # Записываем заголовок в CSV файл
        writer.writerows(json_data) # Записываем все данные из json_data в CSV файл построчно

def csv_to_json(csv_path: str, json_path: str) -> None:
    if not is_valid_csv_file(csv_path):
        print("ValueError: Input file is not a valid CSV or is empty")
        sys.exit(1)

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Создаем объект DictReader для чтения CSV в виде словарей
        data = list(reader) # Читаем все строки и преобразуем в список словарей
    
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4) #разрешаем Unicode символы м красиво форматирум с отпступом 4 пробела
csv_to_json(r"C:\Users\HONOR\Documents\GitHub\laba_prog\data\samples\people.csv",r"C:\Users\HONOR\Documents\GitHub\laba_prog\data\out\people_from_csv.json")

json_to_csv( r"C:\Users\HONOR\Documents\GitHub\laba_prog\data\samples\people.json",  r"C:\Users\HONOR\Documents\GitHub\laba_prog\data\out\people_from_json.csv" )
```
![Картинка 1](./images/image01.png)
![Картинка 1](./images/image02.png)
![Картинка 1](./images/image03.png)
![Картинка 1](./images/image04.png)

### Задание B — CSV → XLSX

```python
import os
import csv
import sys

from openpyxl import Workbook #из библиотеки openpyx1 импортирует только класс Workbook для создаия Excel файлов

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None: #функция конвертанции CSV в XLSX
    if not os.path.exists(csv_path): #если не существует файл по указанному пути, то 
        print("FileNotFoundError") #выводит сообщение об ошибке
        sys.exit(1) #завершает программу с кодом ошибки 1

    if os.path.getsize(csv_path) == 0: #получает размер в байтах и проверяет не равен ли он 0 (пустой файл) 
        print("ValueError")
        sys.exit(1)
    wb = Workbook() #создаем новую Excel книгу
    ws = wb.active #берем первый лист 
    ws.title = "Sheet1" #переменовываем лист в Sheet1

    with open(csv_path, "r", encoding="utf-8") as csv_file: #безопасно открывае файл для прочтения(автомвтически закрывает после использовния #csv_path - путь к файлу
        reader = csv.reader(csv_file) #создает объект для чтения CSV файла
        for row in reader: #перебирает каждую строку в CSV файле, row - переменная, содержащая данные одной строки(как список)
            ws.append(row) #добавляет строку данных в Excel лист

#Настройка ширины колонок
    for column_cells in ws.columns: #перебирает содержания ячейки одной колонки и возвращает все колонки листа 
        max_length = 0 #создает переменную для хранения максимальной длины теста в колонке 
        column_letter = column_cells[0].column_letter #присваивает букву колонки
        for cell in column_cells: #перебирает все ячейки в текущей колонке
            if cell.value: #проверяет есть ли значение в ячейки(не пустая)
                max_length = max(max_length, len(str(cell.value))) #обновляет длину строкиб сравнивая прошлое значение с настоящим 
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8) #обращается к настройкам ширины конкретной колонки, устанавливает ширину колонки, максимальная длина + 2 символа для отступа, 8- выбирает большее значение между расчитанной шириной и минимальной шириной 8 
    wb.save(xlsx_path) #сохраняет Excel книгу по указанному пути
csv_to_xlsx(r"C:\Users\darin\Documents\GitHub\python_labs\date\samples\cities.csv", r"C:\Users\darin\Documents\GitHub\python_labs\date\out\people.xlsx")    
```
![Картинка 1](./images/image05.png)
![Картинка 1](./images/image06.png)