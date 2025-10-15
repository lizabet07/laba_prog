import re
def tokenize(text: str) -> list[str]:
    if not isinstance(text,str):
        raise TypeError
    tokens = re.findall(r'[\w-]+', text) 
    return tokens
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))