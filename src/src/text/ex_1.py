import re  # модуль для работы с регулярными выражениями

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not isinstance(text, str):
        raise TypeError

    text = re.sub(r'\s+', ' ', text)

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    if casefold:
        text = text.casefold()

    return text.strip()
print(normalize("ПрИвЕт\nМИр\t"))        
print(normalize("ёжик, Ёлка")) 
print(normalize("Hello\r\nWorld"))      
print(normalize("  двойные   пробелы  "))