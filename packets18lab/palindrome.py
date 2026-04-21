from .utils import my_split, clean_word


def is_palindrome(word: str) -> bool:
    """
    Проверяет, является ли слово палиндромом
    """
    cleaned = clean_word(word).lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def remove_palindromes(text: str) -> str:
    """
    4) Удаляет из строки слова-палиндромы.
    Возвращает новую строку без этих слов.
    """
    words = my_split(text)
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
