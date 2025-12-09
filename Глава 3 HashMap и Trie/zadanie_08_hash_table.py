"""
Задание 8. Своя хэш-таблица
Реализовать:
- хэш-функцию для строк,
- метод разрешения коллизий (цепочки),
- функции put(key, value), get(key), remove(key).
Визуализировать состояние таблицы после серии вставок.
"""


class HashTable:
    """Хэш-таблица с методом цепочек для разрешения коллизий."""
    
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def hash(self, key):
        """
        Хэш-функция для строк.
        Использует полиномиальную хэш-функцию с множителем 31.
        Трудоемкость: O(len(key))
        """
        hash_value = 0
        for char in str(key):
            hash_value = (hash_value * 31 + ord(char)) % self.capacity
        return hash_value
    
    def put(self, key, value):
        """
        Вставка или обновление пары ключ-значение.
        Трудоемкость: O(1) в среднем, O(n) в худшем случае.
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        
        # Проверяем, есть ли уже такой ключ
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Обновляем значение
                return
        
        # Ключа нет, добавляем новую пару
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key):
        """
        Получение значения по ключу.
        Трудоемкость: O(1) в среднем, O(n) в худшем случае.
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Ключ '{key}' не найден")
    
    def remove(self, key):
        """
        Удаление пары по ключу.
        Трудоемкость: O(1) в среднем, O(n) в худшем случае.
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return v
        
        raise KeyError(f"Ключ '{key}' не найден")
    
    def contains(self, key):
        """Проверка наличия ключа."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def visualize(self):
        """Визуализация состояния хэш-таблицы."""
        print(f"\nСостояние хэш-таблицы (размер: {self.size}, вместимость: {self.capacity}):")
        print("=" * 60)
        
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items = ', '.join([f"({k}: {v})" for k, v in bucket])
                print(f"  Bucket {i:2d}: [{items}]")
            else:
                print(f"  Bucket {i:2d}: []")
        
        print("=" * 60)
        
        # Статистика
        non_empty = sum(1 for b in self.buckets if b)
        max_chain = max(len(b) for b in self.buckets) if self.buckets else 0
        avg_chain = self.size / non_empty if non_empty > 0 else 0
        load_factor = self.size / self.capacity
        
        print(f"\nСтатистика:")
        print(f"  Непустых бакетов: {non_empty}/{self.capacity}")
        print(f"  Макс. длина цепочки: {max_chain}")
        print(f"  Средняя длина цепочки: {avg_chain:.2f}")
        print(f"  Фактор загрузки: {load_factor:.2f}")


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          ТЕСТИРОВАНИЕ ХЭШ-ТАБЛИЦЫ")
    print("="*60)
    
    # Создание хэш-таблицы
    ht = HashTable(capacity=8)
    
    print("\n1. Вставка элементов:")
    items = [
        ("apple", 5),
        ("banana", 3),
        ("cherry", 7),
        ("date", 2),
        ("elderberry", 4),
        ("fig", 6),
        ("grape", 9),
    ]
    
    for key, value in items:
        ht.put(key, value)
        print(f"   put('{key}', {value})")
    
    ht.visualize()
    
    print("\n2. Получение значений:")
    for key, _ in items[:3]:
        value = ht.get(key)
        print(f"   get('{key}') = {value}")
    
    print("\n3. Обновление значения:")
    ht.put("apple", 10)
    print(f"   put('apple', 10)")
    print(f"   get('apple') = {ht.get('apple')}")
    
    print("\n4. Удаление элемента:")
    removed = ht.remove("banana")
    print(f"   remove('banana') = {removed}")
    
    ht.visualize()
    
    print("\n5. Демонстрация коллизий:")
    ht2 = HashTable(capacity=4)
    
    test_keys = ["cat", "dog", "bird", "fish", "mouse", "lion"]
    for key in test_keys:
        hash_val = ht2.hash(key)
        ht2.put(key, len(key))
        print(f"   '{key}' -> hash={hash_val}, length={len(key)}")
    
    ht2.visualize()
    
    print("\n6. Сравнение хороших и плохих хэш-функций:")
    
    # Плохая хэш-функция (всегда возвращает 1)
    class BadHashTable(HashTable):
        def hash(self, key):
            return 1  # Все ключи в один бакет!
    
    print("\n   Плохая хэш-функция (все в один бакет):")
    bad_ht = BadHashTable(capacity=8)
    for key, value in items:
        bad_ht.put(key, value)
    bad_ht.visualize()
    
    print("\n   Хорошая хэш-функция (равномерное распределение):")
    good_ht = HashTable(capacity=8)
    for key, value in items:
        good_ht.put(key, value)
    good_ht.visualize()
