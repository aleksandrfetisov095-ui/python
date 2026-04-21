from .utils import get_words_manual, clean_word

def find_longest_words(text: str) -> list:
    """
    Находит все слова максимальной длины.
    """
    words = get_words_manual(text)
    if len(words) == 0:
        return []
    
    #Максимальная длина
    max_len = 0
    for w in words:
        cleaned = clean_word(w)
        if len(cleaned) > max_len:
            max_len = len(cleaned)
            
    #Собираем слова этой длины
    result = []
    seen_cleaned = [] # Список уже очищенных слов, чтобы не дублировать
    
    for w in words:
        cleaned = clean_word(w)
        
        # Проверка: длина совпадает И слово еще не добавлено
        is_duplicate = False
        for seen in seen_cleaned:
            if seen == cleaned:
                is_duplicate = True
                break
                
        if len(cleaned) == max_len and not is_duplicate:
            result.append(w)       # Добавляем оригинальное слово
            seen_cleaned.append(cleaned) # Запоминаем очищенное
            
    return result
