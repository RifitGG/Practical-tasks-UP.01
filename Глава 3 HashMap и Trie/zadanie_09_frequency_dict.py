"""
Задание 9. Частотный словарь
Построить HashMap частот встречаемости слов в тексте.
Вывести топ-10 самых частых слов.
Сравнить время построения при плохой и хорошей хэш-функции.
"""

import time
import re
from zadanie_08_hash_table import HashTable


def buildFrequencyDict(text):
    """
    Построение частотного словаря слов.
    Трудоемкость: O(n), где n - количество слов.
    """
    freq_dict = {}
    words = re.findall(r'\b\w+\b', text.lower())
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    return freq_dict


def getTopN(freq_dict, n=10):
    """Получение топ-N самых частых слов."""
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:n]


def compareHashFunctions():
    """Сравнение плохой и хорошей хэш-функций."""
    
    # Генерация тестового текста
    words = ["python", "data", "structure", "algorithm", "hash", "table", 
             "search", "sort", "tree", "graph"] * 1000
    
    text = " ".join(words)
    
    print("\n=== Сравнение хэш-функций ===\n")
    print(f"Размер текста: {len(words)} слов\n")
    
    # Плохая хэш-функция
    class BadHashTable(HashTable):
        def hash(self, key):
            return 1
    
    print("1. Плохая хэш-функция (все в один бакет):")
    bad_ht = BadHashTable(capacity=16)
    
    start = time.time()
    for word in words:
        if bad_ht.contains(word):
            count = bad_ht.get(word)
            bad_ht.put(word, count + 1)
        else:
            bad_ht.put(word, 1)
    bad_time = time.time() - start
    
    print(f"   Время: {bad_time:.4f} сек")
    
    # Хорошая хэш-функция
    print("\n2. Хорошая хэш-функция:")
    good_ht = HashTable(capacity=16)
    
    start = time.time()
    for word in words:
        if good_ht.contains(word):
            count = good_ht.get(word)
            good_ht.put(word, count + 1)
        else:
            good_ht.put(word, 1)
    good_time = time.time() - start
    
    print(f"   Время: {good_time:.4f} сек")
    print(f"\n   Ускорение: {bad_time / good_time:.1f}x")


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          ЧАСТОТНЫЙ АНАЛИЗ ТЕКСТА")
    print("="*60)
    
    sample_text = """
    Python is an amazing programming language. Python is widely used
    for data science, machine learning, and web development. Many developers
    love Python because of its simplicity and readability. Python has
    a large community and extensive libraries. Data structures in Python
    are powerful and flexible. Learning data structures is essential
    for becoming a better programmer.
    """
    
    print("\n1. Исходный текст:")
    print(sample_text)
    
    print("\n2. Построение частотного словаря:")
    freq_dict = buildFrequencyDict(sample_text)
    
    print(f"   Уникальных слов: {len(freq_dict)}")
    print(f"   Всего слов: {sum(freq_dict.values())}")
    
    print("\n3. Топ-10 самых частых слов:")
    top_words = getTopN(freq_dict, 10)
    
    for i, (word, count) in enumerate(top_words, 1):
        print(f"   {i:2d}. {word:15} - {count:3d} раз")
    
    compareHashFunctions()
