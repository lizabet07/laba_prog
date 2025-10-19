from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    try:
        return Path(path).read_text(encoding=encoding)
    except FileExistsError:
        return 'Такого файла нету'
    except UnicodeDecodeError:
        return 'Неудалось изменить кодировку'

import csv                     # Модуль для работы с CSV-файлами (чтение и запись)
from pathlib import Path        # Класс Path для удобной работы с путями к файлам
from typing import Sequence     # Тип-подсказка (необязательно, просто для читаемости кода)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)              # Превращаем строку пути в объект Path (удобно работать)
    rows = list(rows)           # Превращаем rows в список (на случай, если это генератор)

    # Проверяем, что все строки одинаковой длины
    if rows:                    # Если список строк не пустой
        length = len(rows[0])   # Берём длину первой строки
        for i, row in enumerate(rows, start=1):  # Перебираем все строки с нумерацией
            if len(row) != length:               # Если длина строки отличается от первой
                # Вызываем ошибку, потому что CSV должен быть "прямоугольным"
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалось {length}")

    # Создаём родительские папки при необходимости
    if not p.parent.exists():                   # Если папка, где должен лежать файл, не существует
        p.parent.mkdir(parents=True, exist_ok=True)  # Создаём её (включая вложенные каталоги)

    # Записываем CSV
    with p.open("w", newline="", encoding="utf-8") as f:  # Открываем файл для записи в UTF-8
        writer = csv.writer(f)                 # Создаём CSV-писатель (будет ставить запятые)
        if header is not None:                 # Если передан заголовок
            writer.writerow(header)            # Записываем первую строку — заголовок
        for row in rows:                       # Проходим по всем строкам данных
            writer.writerow(row)               # Записываем каждую строку в CSV-файл  


from pathlib import Path

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)                           # превращаем путь в объект Path
    if p.parent and not p.parent.exists():   # если у файла есть папка и она не существует
        p.parent.mkdir(parents=True, exist_ok=True)  # создаём все недостающие папки
