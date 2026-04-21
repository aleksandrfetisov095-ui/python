from .utils import my_split, clean_word


def find_most_frequent_in_two(str1: str, str2: str) -> str | None:
    """
    2) Определяет слово, которое чаще всех встречается в двух строках.
    """
    words1 = my_split(str1)
    words2 = my_split(str2)
    all_words = words1 + words2

    counts = {}
    for w in all_words:
        cleaned = clean_word(w).lower()
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1

    most_freq_word = ""
    max_count = 0
    for word, count in counts.items():
        if count > max_count:
            max_count = count
            most_freq_word = word

    return most_freq_word


def find_common_words(str1: str, str2: str) -> list[str]:
    """
    3) Определяет общие для двух строк слова.
    """
    words1 = my_split(str1)
    words2 = my_split(str2)

    cleaned1 = []
    for w in words1:
        cleaned = clean_word(w).lower()
        if cleaned:
            cleaned1.append(cleaned)

    cleaned2 = []
    for w in words2:
        cleaned = clean_word(w).lower()
        if cleaned:
            cleaned2.append(cleaned)

    common = []
    for word1 in cleaned1:
        for word2 in cleaned2:
            if word1 == word2:
                common.append(word1)
                break
    return common
