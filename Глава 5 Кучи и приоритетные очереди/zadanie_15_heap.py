"""
Задание 15. Куча
Реализовать бинарную мин-кучу: вставку, извлечение минимума, построение кучи из массива.
Проверить корректность свойств кучи после каждой операции.
"""


class MinHeap:
    """Бинарная мин-куча."""
    
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        """Индекс родителя."""
        return (i - 1) // 2
    
    def left(self, i):
        """Индекс левого потомка."""
        return 2 * i + 1
    
    def right(self, i):
        """Индекс правого потомка."""
        return 2 * i + 2
    
    def insert(self, value):
        """Вставка элемента. O(log n)."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        """Всплытие элемента вверх."""
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            parent_idx = self.parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx
    
    def extract_min(self):
        """Извлечение минимума. O(log n)."""
        if not self.heap:
            raise IndexError("Куча пуста")
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._sift_down(0)
        
        return min_val
    
    def _sift_down(self, i):
        """Просеивание элемента вниз."""
        min_index = i
        left_idx = self.left(i)
        right_idx = self.right(i)
        
        if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[min_index]:
            min_index = left_idx
        
        if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[min_index]:
            min_index = right_idx
        
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._sift_down(min_index)
    
    def heapify(self, arr):
        """Построение кучи из массива. O(n)."""
        self.heap = arr.copy()
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)
    
    def is_valid(self):
        """Проверка корректности свойств кучи."""
        for i in range(len(self.heap)):
            left_idx = self.left(i)
            right_idx = self.right(i)
            
            if left_idx < len(self.heap) and self.heap[i] > self.heap[left_idx]:
                return False
            if right_idx < len(self.heap) and self.heap[i] > self.heap[right_idx]:
                return False
        
        return True
    
    def peek(self):
        """Просмотр минимума без удаления."""
        if not self.heap:
            raise IndexError("Куча пуста")
        return self.heap[0]
    
    def __str__(self):
        return f"MinHeap({self.heap})"


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          БИНАРНАЯ МИН-КУЧА")
    print("="*60)
    
    heap = MinHeap()
    
    print("\n1. Вставка элементов:")
    values = [5, 3, 8, 1, 9, 2, 7]
    for val in values:
        heap.insert(val)
        print(f"   insert({val}): {heap}, валидна: {heap.is_valid()}")
    
    print("\n2. Просмотр минимума:")
    print(f"   peek() = {heap.peek()}")
    
    print("\n3. Извлечение минимумов:")
    while len(heap.heap) > 0:
        min_val = heap.extract_min()
        valid = heap.is_valid()
        print(f"   extract_min() = {min_val}, осталось: {heap}, валидна: {valid}")
    
    print("\n4. Построение кучи из массива (heapify):")
    arr = [9, 5, 6, 2, 3, 7, 1, 4, 8]
    print(f"   Массив: {arr}")
    heap.heapify(arr)
    print(f"   Куча:   {heap}")
    print(f"   Валидна: {heap.is_valid()}")
    
    print("\n5. Сортировка кучей (Heap Sort):")
    sorted_arr = []
    while len(heap.heap) > 0:
        sorted_arr.append(heap.extract_min())
    print(f"   Отсортированный массив: {sorted_arr}")
