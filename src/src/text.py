import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = re.sub(r'\s+', ' ', text)        # заменяем все пробелы и переводы строк на один пробел
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    return text.strip()                     # убираем пробелы в начале и конце

def tokenize(text: str) -> list[str]:
    return re.findall(r'[\w-]+', text)      # находим все слова и числа

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))            # считаем частоты слов

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)[:n]
