from collections import Counter  # ф-ия для подсчёта повторений
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = Counter(tokens)
    return dict(freq) #превращаем в словарь
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    # 1)проверащаем в список с кортежами, 2)сортируем по частоте, потом по токенам
    return sorted_items[:n]
freq1 = count_freq(["a","b","a","c","b","a"])
freq2 = count_freq(["bb","aa","bb","aa","cc"])
print(top_n(freq1, n = 2))
print(top_n(freq2, n =2))