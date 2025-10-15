import sys
from text import *
def stats(text):

    # Нормализация текста
    text = normalize(text)

    # Разбиваем на слова
    tokens = tokenize(text)

    # Подсчёт частот
    freq = count_freq(tokens)

    # Топ-5 слов
    top = top_n(freq, n=5)

    # Вывод статистики
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")

text_in = sys.stdin.buffer.read().decode('utf-8')
stats(text_in)
