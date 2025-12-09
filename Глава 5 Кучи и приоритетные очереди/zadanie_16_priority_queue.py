"""
Задание 16. Приоритетная очередь
Используя heap, реализовать: push(value, priority), pop().
Применить к задаче: планирование задач, поиск k минимальных элементов массива.
"""

from zadanie_15_heap import MinHeap


class PriorityQueue:
    """Приоритетная очередь на основе мин-кучи."""
    
    def __init__(self):
        self.heap = MinHeap()
    
    def push(self, value, priority):
        """Добавление элемента с приоритетом. O(log n)."""
        self.heap.insert((priority, value))
    
    def pop(self):
        """Извлечение элемента с наименьшим приоритетом. O(log n)."""
        priority, value = self.heap.extract_min()
        return value
    
    def peek(self):
        """Просмотр элемента с наименьшим приоритетом без удаления."""
        priority, value = self.heap.peek()
        return value
    
    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return len(self.heap.heap) == 0
    
    def size(self):
        """Размер очереди."""
        return len(self.heap.heap)


def task_scheduling_demo():
    """Демонстрация планирования задач."""
    print("\n" + "="*60)
    print("          ПЛАНИРОВАНИЕ ЗАДАЧ")
    print("="*60)
    
    pq = PriorityQueue()
    
    tasks = [
        ("Ответить на email", 3),
        ("Срочный баг", 1),
        ("Код-ревью", 2),
        ("Совещание", 2),
        ("Документация", 4),
        ("Критичный баг", 1),
    ]
    
    print("\n1. Добавление задач:")
    for task, priority in tasks:
        pq.push(task, priority)
        print(f"   [{priority}] {task}")
    
    print("\n2. Выполнение задач по приоритету:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"   Выполняется: {task}")


def find_k_smallest(arr, k):
    """
    Поиск k минимальных элементов массива.
    Трудоемкость: O(n log k).
    """
    # Используем макс-кучу размером k
    max_heap = []
    
    for num in arr:
        if len(max_heap) < k:
            max_heap.append(-num)  # Отрицательные для макс-кучи через мин-кучу
            max_heap.sort()
        elif -num > max_heap[0]:  # num < -max_heap[0]
            max_heap[0] = -num
            max_heap.sort()
    
    return sorted([-x for x in max_heap])


def find_k_smallest_heap(arr, k):
    """Поиск k минимальных с использованием кучи."""
    heap = MinHeap()
    heap.heapify(arr)
    
    result = []
    for _ in range(min(k, len(arr))):
        result.append(heap.extract_min())
    
    return result


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          ПРИОРИТЕТНАЯ ОЧЕРЕДЬ")
    print("="*60)
    
    # Базовое использование
    pq = PriorityQueue()
    
    print("\n1. Добавление элементов с приоритетами:")
    items = [("Task A", 5), ("Task B", 2), ("Task C", 8), ("Task D", 1)]
    
    for task, priority in items:
        pq.push(task, priority)
        print(f"   push('{task}', {priority})")
    
    print("\n2. Извлечение по приоритету:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"   pop() = '{task}'")
    
    # Планирование задач
    task_scheduling_demo()
    
    # Поиск k минимальных
    print("\n" + "="*60)
    print("          ПОИСК K МИНИМАЛЬНЫХ ЭЛЕМЕНТОВ")
    print("="*60)
    
    arr = [7, 10, 4, 3, 20, 15, 8, 2]
    k = 3
    
    print(f"\nМассив: {arr}")
    print(f"k = {k}")
    
    result = find_k_smallest_heap(arr, k)
    print(f"\n{k} минимальных элементов: {result}")
    
    # Большой массив
    import random
    large_arr = [random.randint(1, 1000) for _ in range(100)]
    k = 10
    
    print(f"\nБольшой массив из {len(large_arr)} элементов")
    print(f"k = {k}")
    
    result = find_k_smallest_heap(large_arr, k)
    print(f"\n{k} минимальных: {result}")
    
    print("\n" + "="*60)
    print("Применение приоритетных очередей:")
    print("• Планирование задач в ОС")
    print("• Алгоритм Дейкстры (кратчайшие пути)")
    print("• Сжатие данных (код Хаффмана)")
    print("• Поиск k-ых элементов")
    print("• Слияние k отсортированных массивов")
    print("• Обработка событий в симуляциях")
