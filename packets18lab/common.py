from .utils import get_words_manual, clean_word


def find_most_frequent_in_two(str1: str, str2: str) -> str | None:
    """
    2) Определяет слово, которое чаще всех встречается в двух строках.
    """
    words1 = get_words_manual(str1)
    words2 = get_words_manual(str2)
    all_words = words1 + words2

    if not all_words:
        return None

    counts = {}
    for w in all_words:
        cleaned = clean_word(w).lower()  # Приводим к нижнему регистру для учета регистра
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1

    if not counts:
        return None

    max_count = 0
    most_freq_word = ""

    for word, count in counts.items():
        if count > max_count:
            max_count = count
            most_freq_word = word

    return most_freq_word


def find_common_words(str1: str, str2: str) -> list[str]:
    """
    3) Определяет общие для двух строк слова.
    """
    words1 = get_words_manual(str1)
    words2 = get_words_manual(str2)

    set1 = {clean_word(w).lower() for w in words1 if clean_word(w)}
    set2 = {clean_word(w).lower() for w in words2 if clean_word(w)}

    common = set1 & set2

    return list(common)
