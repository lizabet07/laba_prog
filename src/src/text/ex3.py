from collections import Counter  # удобный класс для подсчёта повторений

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = Counter(tokens)
    return dict(freq)

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    def sort_rule(item):
        word = item[0]
        count = item[1]
        return(count,word)
    sorted_items = sorted(freq.items(), key=sort_rule, reverse=True)
    return sorted_items[:n]
tokens1 = ["a","b","a","c","b","a"]
tokens2 = ["bb","aa","bb","aa","cc"]
freq1 = count_freq(["a","b","a","c","b","a"])
freq2 = count_freq(["bb","aa","bb","aa","cc"])
print(count_freq(["a","b","a","c","b","a"]))
print(top_n(freq1, n = 2))
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n(freq2, n =2))