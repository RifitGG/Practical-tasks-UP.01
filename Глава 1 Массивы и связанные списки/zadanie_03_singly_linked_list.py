"""
Задание 3. Односвязный список
Реализовать:
- вставку в начало/конец,
- удаление по значению,
- поиск по значению,
- разворот списка in-place.
Сравнить операции вставки/удаления с массивом.
"""

import time


class Node:
    """Узел односвязного списка."""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Односвязный список."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def pushFront(self, data):
        """
        Вставка элемента в начало списка.
        Трудоемкость: O(1) - создание узла и обновление ссылок.
        """
        new_node = Node(data)
        
        if self.head is None:
            # Список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # Вставляем в начало
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
    
    def pushBack(self, data):
        """
        Вставка элемента в конец списка.
        Трудоемкость: O(1) - при наличии указателя tail.
        Без указателя tail потребовалось бы O(n) для поиска последнего узла.
        """
        new_node = Node(data)
        
        if self.head is None:
            # Список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # Вставляем в конец
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def removeByValue(self, value):
        """
        Удаление первого узла с заданным значением.
        Трудоемкость: O(n) - требуется поиск узла.
        
        Returns:
            True, если элемент найден и удален, иначе False.
        """
        if self.head is None:
            return False
        
        # Особый случай: удаление головы
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True
        
        # Поиск узла для удаления
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                # Найден узел для удаления
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, value):
        """
        Поиск элемента по значению.
        Трудоемкость: O(n) - последовательный перебор узлов.
        
        Returns:
            Индекс найденного элемента или -1, если не найден.
        """
        current = self.head
        index = 0
        
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def reverse(self):
        """
        Разворот списка in-place.
        Трудоемкость: O(n) - один проход по списку с изменением направления ссылок.
        """
        if self.head is None or self.head.next is None:
            return  # Пустой список или один элемент
        
        # Сохраняем старый хвост (он станет головой)
        self.tail = self.head
        
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  # Сохраняем следующий узел
            current.next = prev       # Переворачиваем ссылку
            prev = current            # Двигаемся вперед
            current = next_node
        
        self.head = prev
    
    def toList(self):
        """Преобразование связного списка в Python list для удобства."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self):
        """Строковое представление списка."""
        if self.head is None:
            return "LinkedList([])"
        
        elements = self.toList()
        if len(elements) > 10:
            return f"LinkedList([{', '.join(map(str, elements[:5]))} ... {', '.join(map(str, elements[-5:]))}], size={self.size})"
        return f"LinkedList({elements})"
    
    def __len__(self):
        return self.size


def compare_with_array():
    """Сравнение операций вставки/удаления со списком и массивом."""
    N = 10000
    
    print("\n=== Сравнение односвязного списка и массива ===\n")
    
    # Тест 1: Вставка в начало
    print(f"1. Вставка {N} элементов в НАЧАЛО:")
    
    # Односвязный список
    linked_list = LinkedList()
    start_time = time.time()
    for i in range(N):
        linked_list.pushFront(i)
    ll_time = time.time() - start_time
    print(f"   Односвязный список: {ll_time:.4f} сек")
    
    # Python list (эквивалент динамического массива)
    array = []
    start_time = time.time()
    for i in range(N):
        array.insert(0, i)  # Вставка в начало
    arr_time = time.time() - start_time
    print(f"   Массив (list):      {arr_time:.4f} сек")
    print(f"   Односвязный список быстрее в {arr_time / ll_time:.1f}x раз")
    
    # Тест 2: Вставка в конец
    print(f"\n2. Вставка {N} элементов в КОНЕЦ:")
    
    linked_list = LinkedList()
    start_time = time.time()
    for i in range(N):
        linked_list.pushBack(i)
    ll_time = time.time() - start_time
    print(f"   Односвязный список: {ll_time:.4f} сек")
    
    array = []
    start_time = time.time()
    for i in range(N):
        array.append(i)
    arr_time = time.time() - start_time
    print(f"   Массив (list):      {arr_time:.4f} сек")
    print(f"   Примерно одинаковая производительность (обе O(1))")
    
    # Тест 3: Удаление из начала
    print(f"\n3. Удаление {N//2} элементов из НАЧАЛА:")
    
    # Односвязный список
    linked_list = LinkedList()
    for i in range(N):
        linked_list.pushBack(i)
    
    start_time = time.time()
    for i in range(N // 2):
        linked_list.removeByValue(i)
    ll_time = time.time() - start_time
    print(f"   Односвязный список: {ll_time:.4f} сек")
    
    # Массив
    array = list(range(N))
    start_time = time.time()
    for i in range(N // 2):
        array.remove(i)
    arr_time = time.time() - start_time
    print(f"   Массив (list):      {arr_time:.4f} сек")
    
    print("\n=== Выводы ===")
    print("✓ Вставка в начало: односвязный список O(1) vs массив O(n)")
    print("✓ Вставка в конец: обе структуры O(1)")
    print("✓ Удаление: односвязный список лучше при удалении из начала")
    print("✗ Доступ по индексу: массив O(1) vs односвязный список O(n)")


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование односвязного списка ===\n")
    
    # Создание списка
    ll = LinkedList()
    
    # Тест вставки в начало
    print("1. Вставка элементов в начало (pushFront):")
    for i in range(5):
        ll.pushFront(i)
    print(f"   {ll}")
    
    # Тест вставки в конец
    print("\n2. Вставка элементов в конец (pushBack):")
    for i in range(5, 10):
        ll.pushBack(i)
    print(f"   {ll}")
    
    # Тест поиска
    print("\n3. Поиск элемента со значением 7:")
    index = ll.find(7)
    print(f"   Найден на позиции: {index}")
    
    # Тест удаления
    print("\n4. Удаление элемента со значением 4:")
    removed = ll.removeByValue(4)
    print(f"   Удален: {removed}")
    print(f"   {ll}")
    
    # Тест удаления из начала
    print("\n5. Удаление элемента из начала (значение 0):")
    removed = ll.removeByValue(0)
    print(f"   Удален: {removed}")
    print(f"   {ll}")
    
    # Тест удаления из конца
    print("\n6. Удаление элемента из конца (значение 9):")
    removed = ll.removeByValue(9)
    print(f"   Удален: {removed}")
    print(f"   {ll}")
    
    # Тест разворота списка
    print("\n7. Разворот списка (reverse):")
    print(f"   До разворота:  {ll}")
    ll.reverse()
    print(f"   После разворота: {ll}")
    
    # Еще один разворот для проверки
    print("\n8. Повторный разворот:")
    ll.reverse()
    print(f"   {ll}")
    
    # Тест разворота маленького списка
    print("\n9. Разворот списка из 3 элементов:")
    small_ll = LinkedList()
    small_ll.pushBack(1)
    small_ll.pushBack(2)
    small_ll.pushBack(3)
    print(f"   До:    {small_ll}")
    small_ll.reverse()
    print(f"   После: {small_ll}")
    
    # Сравнение с массивом
    compare_with_array()
    
    print("\n=== Анализ трудоемкости ===")
    print("pushFront:       O(1) - обновление head")
    print("pushBack:        O(1) - обновление tail")
    print("removeByValue:   O(n) - поиск элемента")
    print("find:            O(n) - последовательный поиск")
    print("reverse:         O(n) - один проход по списку")
