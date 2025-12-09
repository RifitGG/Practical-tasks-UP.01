"""
Задание 4. Двусвязный список
Реализовать:
- вставку после произвольного узла,
- удаление узла без поиска "сначала",
- итератор по двусвязному списку.
"""


class DoublyNode:
    """Узел двусвязного списка."""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Двусвязный список."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def pushFront(self, data):
        """
        Вставка элемента в начало списка.
        Трудоемкость: O(1).
        """
        new_node = DoublyNode(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
        return new_node
    
    def pushBack(self, data):
        """
        Вставка элемента в конец списка.
        Трудоемкость: O(1).
        """
        new_node = DoublyNode(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        return new_node
    
    def insertAfter(self, node, data):
        """
        Вставка элемента после заданного узла.
        Трудоемкость: O(1) - если есть прямая ссылка на узел.
        
        Args:
            node: узел, после которого вставляем
            data: данные для нового узла
        
        Returns:
            Новый узел
        """
        if node is None:
            raise ValueError("Узел не может быть None")
        
        new_node = DoublyNode(data)
        new_node.prev = node
        new_node.next = node.next
        
        if node.next is not None:
            node.next.prev = new_node
        else:
            # Вставка после последнего узла
            self.tail = new_node
        
        node.next = new_node
        self.size += 1
        
        return new_node
    
    def insertBefore(self, node, data):
        """
        Вставка элемента перед заданным узлом.
        Трудоемкость: O(1).
        
        Args:
            node: узел, перед которым вставляем
            data: данные для нового узла
        
        Returns:
            Новый узел
        """
        if node is None:
            raise ValueError("Узел не может быть None")
        
        new_node = DoublyNode(data)
        new_node.next = node
        new_node.prev = node.prev
        
        if node.prev is not None:
            node.prev.next = new_node
        else:
            # Вставка перед первым узлом
            self.head = new_node
        
        node.prev = new_node
        self.size += 1
        
        return new_node
    
    def removeNode(self, node):
        """
        Удаление узла без предварительного поиска.
        Трудоемкость: O(1) - благодаря двусвязности достаточно обновить ссылки соседей.
        
        Args:
            node: узел для удаления
        
        Returns:
            Данные удаленного узла
        """
        if node is None:
            raise ValueError("Узел не может быть None")
        
        # Обновляем ссылку предыдущего узла
        if node.prev is not None:
            node.prev.next = node.next
        else:
            # Удаляем голову
            self.head = node.next
        
        # Обновляем ссылку следующего узла
        if node.next is not None:
            node.next.prev = node.prev
        else:
            # Удаляем хвост
            self.tail = node.prev
        
        self.size -= 1
        return node.data
    
    def find(self, value):
        """
        Поиск узла по значению.
        Трудоемкость: O(n).
        
        Returns:
            Узел с найденным значением или None
        """
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None
    
    def toList(self):
        """Преобразование в Python list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    def toListReverse(self):
        """Преобразование в Python list в обратном порядке."""
        result = []
        current = self.tail
        while current is not None:
            result.append(current.data)
            current = current.prev
        return result
    
    def __str__(self):
        """Строковое представление списка."""
        if self.head is None:
            return "DoublyLinkedList([])"
        
        elements = self.toList()
        if len(elements) > 10:
            return f"DoublyLinkedList([{', '.join(map(str, elements[:5]))} ... {', '.join(map(str, elements[-5:]))}], size={self.size})"
        return f"DoublyLinkedList({elements})"
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        """
        Прямой итератор: от головы к хвосту.
        Позволяет использовать цикл for для обхода списка.
        """
        return DoublyLinkedListIterator(self.head, forward=True)
    
    def reverse_iter(self):
        """
        Обратный итератор: от хвоста к голове.
        """
        return DoublyLinkedListIterator(self.tail, forward=False)


class DoublyLinkedListIterator:
    """Итератор для двусвязного списка."""
    
    def __init__(self, start_node, forward=True):
        """
        Args:
            start_node: начальный узел
            forward: True для прямого обхода, False для обратного
        """
        self.current = start_node
        self.forward = forward
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        data = self.current.data
        
        if self.forward:
            self.current = self.current.next
        else:
            self.current = self.current.prev
        
        return data


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование двусвязного списка ===\n")
    
    # Создание списка
    dll = DoublyLinkedList()
    
    # Тест базовых операций
    print("1. Добавление элементов:")
    for i in range(5):
        dll.pushBack(i * 10)
    print(f"   {dll}")
    
    # Тест вставки после узла
    print("\n2. Вставка после узла со значением 20:")
    node_20 = dll.find(20)
    if node_20:
        dll.insertAfter(node_20, 999)
    print(f"   {dll}")
    
    # Тест вставки перед узлом
    print("\n3. Вставка перед узлом со значением 30:")
    node_30 = dll.find(30)
    if node_30:
        dll.insertBefore(node_30, 777)
    print(f"   {dll}")
    
    # Тест удаления узла
    print("\n4. Удаление узла со значением 10 (без поиска заново):")
    node_10 = dll.find(10)
    if node_10:
        removed = dll.removeNode(node_10)
        print(f"   Удален: {removed}")
    print(f"   {dll}")
    
    # Тест удаления головы
    print("\n5. Удаление головы (значение 0):")
    head_node = dll.head
    if head_node:
        removed = dll.removeNode(head_node)
        print(f"   Удален: {removed}")
    print(f"   {dll}")
    
    # Тест удаления хвоста
    print("\n6. Удаление хвоста (значение 40):")
    tail_node = dll.tail
    if tail_node:
        removed = dll.removeNode(tail_node)
        print(f"   Удален: {removed}")
    print(f"   {dll}")
    
    # Тест прямого итератора
    print("\n7. Прямой обход списка (используя итератор):")
    print("   ", end="")
    for value in dll:
        print(value, end=" -> ")
    print("None")
    
    # Тест обратного итератора
    print("\n8. Обратный обход списка (используя reverse_iter):")
    print("   ", end="")
    for value in dll.reverse_iter():
        print(value, end=" -> ")
    print("None")
    
    # Сравнение прямого и обратного обхода
    print("\n9. Проверка соответствия обходов:")
    forward_list = list(dll)
    reverse_list = list(dll.reverse_iter())
    print(f"   Прямой:   {forward_list}")
    print(f"   Обратный: {reverse_list}")
    print(f"   Совпадают: {forward_list == reverse_list[::-1]}")
    
    # Создание нового списка для демонстрации итераторов
    print("\n10. Создание списка с числами 1-10:")
    dll2 = DoublyLinkedList()
    for i in range(1, 11):
        dll2.pushBack(i)
    print(f"    {dll2}")
    
    # Использование итератора в list comprehension
    print("\n11. Использование итератора в различных контекстах:")
    
    # Прямой обход
    squares = [x**2 for x in dll2]
    print(f"    Квадраты (прямой обход): {squares}")
    
    # Обратный обход
    cubes = [x**3 for x in dll2.reverse_iter()]
    print(f"    Кубы (обратный обход): {cubes}")
    
    # Фильтрация
    evens = [x for x in dll2 if x % 2 == 0]
    print(f"    Четные числа: {evens}")
    
    # Сумма элементов
    total = sum(dll2)
    print(f"    Сумма всех элементов: {total}")
    
    # Тест производительности удаления
    print("\n12. Демонстрация эффективности удаления узла:")
    dll3 = DoublyLinkedList()
    for i in range(10):
        dll3.pushBack(i)
    
    print(f"    Исходный список: {dll3}")
    
    # Найти средний узел
    middle_node = dll3.find(5)
    print(f"    Удаляем узел со значением 5 (O(1) операция)...")
    dll3.removeNode(middle_node)
    print(f"    Результат: {dll3}")
    
    print("\n=== Преимущества двусвязного списка ===")
    print("✓ Вставка после/перед узлом: O(1)")
    print("✓ Удаление узла без поиска: O(1)")
    print("✓ Обход в обоих направлениях: O(n)")
    print("✓ Двунаправленный итератор")
    print("✗ Больше памяти на хранение (две ссылки вместо одной)")
    
    print("\n=== Анализ трудоемкости ===")
    print("pushFront/pushBack:  O(1)")
    print("insertAfter/Before:  O(1) - при наличии ссылки на узел")
    print("removeNode:          O(1) - при наличии ссылки на узел")
    print("find:                O(n) - поиск узла")
    print("Итерация:            O(n) - в обоих направлениях")
