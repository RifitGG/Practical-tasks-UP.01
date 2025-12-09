"""
Задание 10. Trie + HashMap: автодополнение
Реализовать Trie для хранения слов.
Реализовать поиск по префиксу: метод autocomplete(prefix).
Используя HashMap + Trie: хранить слова + их частоты,
предлагать подсказки в порядке убывания частоты.
"""


class TrieNode:
    """Узел префиксного дерева."""
    
    def __init__(self):
        self.children = {}  # Словарь дочерних узлов
        self.is_end_of_word = False
        self.frequency = 0  # Частота использования слова


class Trie:
    """Префиксное дерево для автодополнения."""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, frequency=1):
        """
        Вставка слова в Trie.
        Трудоемкость: O(len(word))
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.frequency += frequency
    
    def search(self, word):
        """
        Поиск слова в Trie.
        Трудоемкость: O(len(word))
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def _find_node(self, prefix):
        """Поиск узла по префиксу."""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node
    
    def autocomplete(self, prefix, max_results=10):
        """
        Автодополнение по префиксу.
        Возвращает слова, отсортированные по частоте.
        Трудоемкость: O(len(prefix) + m), где m - количество слов с префиксом.
        """
        node = self._find_node(prefix)
        
        if node is None:
            return []
        
        # Собираем все слова с данным префиксом
        results = []
        self._collect_words(node, prefix, results)
        
        # Сортируем по частоте (убывание)
        results.sort(key=lambda x: x[1], reverse=True)
        
        return [word for word, freq in results[:max_results]]
    
    def _collect_words(self, node, prefix, results):
        """Рекурсивный сбор всех слов из поддерева."""
        if node.is_end_of_word:
            results.append((prefix, node.frequency))
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, results)


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          АВТОДОПОЛНЕНИЕ С TRIE")
    print("="*60)
    
    # Создание Trie
    trie = Trie()
    
    # Добавление слов с частотами
    words_with_freq = [
        ("python", 100),
        ("program", 50),
        ("programming", 80),
        ("programmer", 60),
        ("pro", 10),
        ("project", 70),
        ("product", 40),
        ("practice", 30),
        ("java", 90),
        ("javascript", 85),
    ]
    
    print("\n1. Добавление слов в Trie:")
    for word, freq in words_with_freq:
        trie.insert(word, freq)
        print(f"   '{word}' (частота: {freq})")
    
    print("\n2. Поиск слов:")
    test_words = ["python", "program", "pro", "production"]
    for word in test_words:
        found = trie.search(word)
        print(f"   '{word}': {'✓ найдено' if found else '✗ не найдено'}")
    
    print("\n3. Автодополнение:")
    
    test_prefixes = ["pro", "prog", "java", "py", "p"]
    
    for prefix in test_prefixes:
        suggestions = trie.autocomplete(prefix, max_results=5)
        print(f"\n   Префикс '{prefix}':")
        if suggestions:
            for i, word in enumerate(suggestions, 1):
                print(f"      {i}. {word}")
        else:
            print("      (нет предложений)")
    
    print("\n4. Симуляция поискового запроса:")
    query = "program"
    print(f"\n   Пользователь вводит: '{query}'")
    
    for i in range(1, len(query) + 1):
        prefix = query[:i]
        suggestions = trie.autocomplete(prefix, max_results=3)
        print(f"   '{prefix}' -> {suggestions}")
