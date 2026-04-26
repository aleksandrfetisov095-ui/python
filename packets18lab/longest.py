from .utils import my_split, clean_word


def find_longest_words(text: str) -> list[str]:
    """
    1) Определяет самое длинное слово в строке.
    Если слов с максимальной длиной несколько – выводит все.
    """
    words = my_split(text)
    # Находим максимальную длину среди слов
    max_len = 0
    for w in words:
        cleaned = clean_word(w)
        if len(cleaned) > max_len:
            max_len = len(cleaned)

    # Собираем все слова такой длины
    result = []
    seen = set()

    for w in words:
        cleaned = clean_word(w)
        if len(cleaned) == max_len and cleaned not in seen:
            result.append(w)
            seen.add(cleaned)

    return result
