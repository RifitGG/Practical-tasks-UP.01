"""
Задание 6. Очередь
Реализовать очередь на:
- циклическом массиве,
- двух стеках.
"""


class CircularQueue:
    """Очередь на основе циклического массива."""
    
    def __init__(self, capacity=10):
        """
        Инициализация циклической очереди.
        
        Args:
            capacity: максимальная вместимость очереди
        """
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0  # Индекс начала очереди
        self.rear = 0   # Индекс конца очереди
        self.size = 0   # Текущий размер
    
    def enqueue(self, value):
        """
        Добавление элемента в конец очереди.
        Трудоемкость: O(1).
        
        Args:
            value: значение для добавления
        
        Raises:
            OverflowError: если очередь заполнена
        """
        if self.isFull():
            raise OverflowError("Очередь заполнена")
        
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity  # Циклический переход
        self.size += 1
    
    def dequeue(self):
        """
        Удаление и возврат элемента из начала очереди.
        Трудоемкость: O(1).
        
        Returns:
            Значение из начала очереди
        
        Raises:
            IndexError: если очередь пуста
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        
        value = self.data[self.front]
        self.data[self.front] = None  # Очищаем ячейку
        self.front = (self.front + 1) % self.capacity  # Циклический переход
        self.size -= 1
        
        return value
    
    def peek(self):
        """
        Просмотр элемента в начале очереди без удаления.
        Трудоемкость: O(1).
        
        Raises:
            IndexError: если очередь пуста
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        return self.data[self.front]
    
    def isEmpty(self):
        """Проверка, пуста ли очередь. O(1)"""
        return self.size == 0
    
    def isFull(self):
        """Проверка, заполнена ли очередь. O(1)"""
        return self.size == self.capacity
    
    def getSize(self):
        """Получение текущего размера. O(1)"""
        return self.size
    
    def __str__(self):
        """Строковое представление очереди."""
        if self.isEmpty():
            return "CircularQueue([])"
        
        elements = []
        index = self.front
        for _ in range(self.size):
            elements.append(self.data[index])
            index = (index + 1) % self.capacity
        
        return f"CircularQueue({elements}, front={self.front}, rear={self.rear}, size={self.size}/{self.capacity})"


class QueueTwoStacks:
    """Очередь на основе двух стеков."""
    
    def __init__(self):
        self.input_stack = []   # Стек для входящих элементов
        self.output_stack = []  # Стек для исходящих элементов
    
    def enqueue(self, value):
        """
        Добавление элемента в конец очереди.
        Трудоемкость: O(1) - просто добавление в input_stack.
        """
        self.input_stack.append(value)
    
    def _transfer(self):
        """
        Перекладывание элементов из input_stack в output_stack.
        Выполняется только когда output_stack пуст.
        """
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())
    
    def dequeue(self):
        """
        Удаление и возврат элемента из начала очереди.
        Трудоемкость: O(1) амортизированная.
        
        В худшем случае O(n), когда нужно перекладывать все элементы,
        но каждый элемент перекладывается максимум один раз, что дает
        амортизированную сложность O(1).
        
        Returns:
            Значение из начала очереди
        
        Raises:
            IndexError: если очередь пуста
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        
        if not self.output_stack:
            self._transfer()
        
        return self.output_stack.pop()
    
    def peek(self):
        """
        Просмотр элемента в начале очереди без удаления.
        Трудоемкость: O(1) амортизированная.
        
        Raises:
            IndexError: если очередь пуста
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        
        if not self.output_stack:
            self._transfer()
        
        return self.output_stack[-1]
    
    def isEmpty(self):
        """Проверка, пуста ли очередь. O(1)"""
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def size(self):
        """Получение размера очереди. O(1)"""
        return len(self.input_stack) + len(self.output_stack)
    
    def __str__(self):
        """Строковое представление очереди."""
        # Элементы в output_stack уже в правильном порядке
        # Элементы в input_stack нужно перевернуть
        elements = list(reversed(self.output_stack)) + self.input_stack
        return f"QueueTwoStacks({elements}, in={self.input_stack}, out={self.output_stack})"


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование циклической очереди ===\n")
    
    # Создание очереди
    queue = CircularQueue(capacity=5)
    
    print("1. Добавление элементов:")
    for i in [10, 20, 30, 40]:
        queue.enqueue(i)
        print(f"   enqueue({i}): {queue}")
    
    print("\n2. Просмотр первого элемента:")
    print(f"   peek(): {queue.peek()}")
    
    print("\n3. Удаление двух элементов:")
    for _ in range(2):
        value = queue.dequeue()
        print(f"   dequeue(): {value}")
        print(f"   Очередь: {queue}")
    
    print("\n4. Демонстрация циклического поведения:")
    print("   Добавляем еще элементы (50, 60, 70)...")
    for i in [50, 60, 70]:
        queue.enqueue(i)
        print(f"   enqueue({i}): {queue}")
    
    print("\n5. Попытка переполнения очереди:")
    try:
        queue.enqueue(80)
    except OverflowError as e:
        print(f"   Ошибка: {e}")
        print(f"   Очередь: {queue}")
    
    print("\n6. Полное опустошение очереди:")
    while not queue.isEmpty():
        value = queue.dequeue()
        print(f"   dequeue(): {value}")
    print(f"   Очередь пуста: {queue.isEmpty()}")
    
    print("\n7. Попытка удаления из пустой очереди:")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"   Ошибка: {e}")
    
    print("\n" + "="*60)
    print("=== Тестирование очереди на двух стеках ===\n")
    
    # Создание очереди на двух стеках
    queue2 = QueueTwoStacks()
    
    print("1. Добавление элементов:")
    for i in ['A', 'B', 'C', 'D', 'E']:
        queue2.enqueue(i)
        print(f"   enqueue('{i}'): {queue2}")
    
    print("\n2. Просмотр первого элемента:")
    print(f"   peek(): {queue2.peek()}")
    print(f"   После peek: {queue2}")
    print("   Обратите внимание: элементы переложены в output_stack")
    
    print("\n3. Удаление трех элементов:")
    for _ in range(3):
        value = queue2.dequeue()
        print(f"   dequeue(): {value}")
        print(f"   Очередь: {queue2}")
    
    print("\n4. Добавление новых элементов:")
    for i in ['F', 'G', 'H']:
        queue2.enqueue(i)
        print(f"   enqueue('{i}'): {queue2}")
    
    print("\n5. Удаление всех оставшихся элементов:")
    while not queue2.isEmpty():
        value = queue2.dequeue()
        print(f"   dequeue(): {value}, размер: {queue2.size()}")
    
    print("\n" + "="*60)
    print("=== Демонстрация амортизированной сложности ===\n")
    
    import time
    
    N = 10000
    
    # Тест циклической очереди
    print(f"1. Циклическая очередь - {N} операций:")
    cq = CircularQueue(capacity=N)
    
    start = time.time()
    for i in range(N):
        cq.enqueue(i)
    for _ in range(N):
        cq.dequeue()
    cq_time = time.time() - start
    
    print(f"   Время: {cq_time:.4f} сек")
    
    # Тест очереди на двух стеках
    print(f"\n2. Очередь на двух стеках - {N} операций:")
    q2s = QueueTwoStacks()
    
    start = time.time()
    for i in range(N):
        q2s.enqueue(i)
    for _ in range(N):
        q2s.dequeue()
    q2s_time = time.time() - start
    
    print(f"   Время: {cq_time:.4f} сек")
    
    print("\n=== Сравнение реализаций ===")
    
    print("\nЦиклическая очередь:")
    print("  ✓ Все операции строго O(1)")
    print("  ✓ Предсказуемая производительность")
    print("  ✓ Эффективное использование памяти")
    print("  ✗ Ограниченная вместимость")
    print("  ✗ Требует заранее знать максимальный размер")
    
    print("\nОчередь на двух стеках:")
    print("  ✓ Неограниченная вместимость")
    print("  ✓ Амортизированная O(1) для всех операций")
    print("  ✓ Простая реализация")
    print("  ~ Иногда операция dequeue занимает O(n)")
    print("  ~ Использует больше памяти (два стека)")
    
    print("\n=== Применение очередей ===")
    print("• Обработка задач в порядке поступления")
    print("• Алгоритм обхода графа в ширину (BFS)")
    print("• Управление буферами (принтеры, сетевые пакеты)")
    print("• Планирование процессов в ОС")
    print("• Кэширование (FIFO)")
    print("• Моделирование реальных очередей (магазины, банки)")
