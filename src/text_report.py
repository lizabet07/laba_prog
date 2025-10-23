import csv
import re
import os #пути и файлы
import sys #работа с путями

# Добавляем путь к корневой папке проекта 
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, project_root)

from lib.text import normalize, tokenize, count_freq, top_n

# Пути к файлам относительно корня проекта
input_path = os.path.join(project_root, 'data', 'input.txt')
output_path = os.path.join(project_root, 'data', 'report.csv')

# Читаем файл
with open(input_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Обрабатываем текст
normalized = normalize(text)
words = tokenize(normalized)
freq = count_freq(words)

# Сохраняем отчет в CSV
sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'count'])
    for word, count in sorted_words:
        writer.writerow([word, count])

# Печатаем резюме
print(f"Всего слов: {len(words)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

top_5 = top_n(freq, 5)
for i, (word, count) in enumerate(top_5, 1):
    print(f"  {i}. {word}: {count}")