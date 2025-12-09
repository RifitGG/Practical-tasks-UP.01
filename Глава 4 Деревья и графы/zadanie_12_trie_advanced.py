"""
Задание 12. Trie (углубление)
Добавить в Trie:
- хранение слов целиком,
- подсчёт количества вариантов по префиксу,
- удаление слова.
"""


class AdvancedTrieNode:
    """Узел расширенного Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None  # Хранение полного слова
        self.count = 0    # Счетчик слов, проходящих через узел


class AdvancedTrie:
    """Расширенное префиксное дерево."""
    
    def __init__(self):
        self.root = AdvancedTrieNode()
    
    def insert(self, word):
        """Вставка слова с обновлением счетчиков."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = AdvancedTrieNode()
            node = node.children[char]
            node.count += 1
        
        node.is_end_of_word = True
        node.word = word
    
    def count_prefix(self, prefix):
        """Количество слов с заданным префиксом. O(len(prefix))."""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.count
    
    def delete(self, word):
        """Удаление слова из Trie."""
        def _delete_recursive(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                node.word = None
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            child = node.children[char]
            child.count -= 1
            
            should_delete = _delete_recursive(child, word, index + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete_recursive(self.root, word, 0)
    
    def get_all_words(self, prefix=""):
        """Получить все слова с заданным префиксом."""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        self._collect_words(node, words)
        return words
    
    def _collect_words(self, node, words):
        if node.is_end_of_word:
            words.append(node.word)
        
        for child in node.children.values():
            self._collect_words(child, words)


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          РАСШИРЕННОЕ TRIE")
    print("="*60)
    
    trie = AdvancedTrie()
    
    words = ["cat", "cats", "dog", "dogs", "catalog", "category"]
    
    print("\n1. Вставка слов:", words)
    for word in words:
        trie.insert(word)
    
    print("\n2. Подсчет слов по префиксу:")
    prefixes = ["cat", "dog", "ca", "d", "x"]
    for prefix in prefixes:
        count = trie.count_prefix(prefix)
        print(f"   '{prefix}': {count} слов")
    
    print("\n3. Получение всех слов по префиксу:")
    for prefix in ["cat", "dog"]:
        words_list = trie.get_all_words(prefix)
        print(f"   '{prefix}': {words_list}")
    
    print("\n4. Удаление слова 'cats':")
    trie.delete("cats")
    print(f"   Слова с 'cat': {trie.get_all_words('cat')}")
    print(f"   Количество с 'cat': {trie.count_prefix('cat')}")
