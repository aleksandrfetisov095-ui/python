
def my_split(text: str) -> list[str]:
    """
    Разбивает строку на список слов.
    Слова разделяются пробелами. Знаки препинания оставляем при словах.
    Для простоты считаем словом последовательность символов до пробела.
    """
    words = []
    current_word = ""

    for char in text:
        if char != ' ':
            current_word += char
        else:
            if current_word:  #накопили символы, сохраняем слово
                words.append(current_word)
                current_word = ""

    #последнее слово, если строка не заканчивается пробелом
    if current_word:
        words.append(current_word)

    return words


def clean_word(word: str) -> str:
    """
    Удаляет знаки препинания по краям слова для корректного сравнения длины и палиндромности.
    """
    chars_to_strip = ".,!?;:-"
    start = 0
    end = len(word)

    while start < end and word[start] in chars_to_strip:
        start += 1
    while end > start and word[end - 1] in chars_to_strip:
        end -= 1

    result = ""
    i = start
    while i < end:
        result += word[i]
        i += 1

    return result
