from collections import Counter
from pathlib import Path
from src.lab04.io_txt_csv import read_text, write_csv
from lib.text.py import normalize, tokenize  # из ЛР3

def main():
    in_path = Path("data/input.txt")
    out_path = Path("data/report.csv")

    # читаем текст
    text = read_text(in_path, encoding="utf-8")

    # нормализуем, токенизируем, считаем частоты
    tokens = tokenize(normalize(text))
    freq = Counter(tokens)

    # сортируем по частоте ↓, слову ↑
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # сохраняем в CSV
    write_csv(sorted_freq, out_path, header=("word", "count"))

    # выводим краткое резюме
    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    top5 = sorted_freq[:5]
    print("Топ-5:", ", ".join(f"{w} ({c})" for w, c in top5))

if name == "__main__":
    main()