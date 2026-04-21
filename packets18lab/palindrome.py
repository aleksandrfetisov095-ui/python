from .utils import get_words_manual, clean_word


def is_palindrome(word: str) -> bool:
    """
    Проверяет, является ли слово палиндромом
    """
    cleaned = clean_word(word).lower()
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]


def remove_palindromes(text: str) -> str:
    """
    4) Удаляет из строки слова-палиндромы.
    Возвращает новую строку без этих слов.
    """
    words = get_words_manual(text)
    new_words = []

    for w in words:
        if not is_palindrome(w):
            new_words.append(w)
    result = ""
    for i, w in enumerate(new_words):
        if i > 0:
            result += " "
        result += w

    return result
