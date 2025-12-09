"""
Задание 2. Динамический массив
Реализовать динамический массив с автоматическим расширением (стратегия увеличения ×2).
Сравнить время вставки 100000 элементов в статический массив vs динамический.
"""

import time


class DynamicArray:
    def __init__(self, initial_capacity=8):
        """
        Инициализация динамического массива.
        
        Args:
            initial_capacity: начальная вместимость массива
        """
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * self.capacity
        self.resize_count = 0  # Счетчик количества расширений
    
    def _resize(self):
        """
        Увеличение ёмкости массива в 2 раза.
        Трудоемкость: O(n) - копирование всех элементов.
        Однако, амортизированная сложность pushBack остается O(1).
        """
        self.capacity *= 2
        new_data = [None] * self.capacity
        
        # Копируем все элементы в новый массив
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data
        self.resize_count += 1
        print(f"   [Расширение массива #{self.resize_count}: новая вместимость = {self.capacity}]")
    
    def pushBack(self, value):
        """
        Добавление элемента в конец массива.
        Трудоемкость: O(1) амортизированная - в среднем константное время,
        хотя иногда требуется O(n) для расширения.
        
        Args:
            value: значение для добавления
        """
        if self.size >= self.capacity:
            self._resize()
        
        self.data[self.size] = value
        self.size += 1
    
    def pushFront(self, value):
        """
        Добавление элемента в начало массива.
        Трудоемкость: O(n) - требуется сдвинуть все элементы.
        """
        if self.size >= self.capacity:
            self._resize()
        
        # Сдвигаем все элементы вправо
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[0] = value
        self.size += 1
    
    def insert(self, index, value):
        """
        Вставка элемента на произвольную позицию.
        Трудоемкость: O(n) - сдвиг части элементов.
        """
        if index < 0 or index > self.size:
            raise IndexError(f"Индекс {index} выходит за границы [0, {self.size}]")
        
        if self.size >= self.capacity:
            self._resize()
        
        # Сдвигаем элементы вправо
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, index):
        """
        Удаление элемента по индексу.
        Трудоемкость: O(n) - сдвиг части элементов.
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Индекс {index} выходит за границы [0, {self.size - 1}]")
        
        removed_value = self.data[index]
        
        # Сдвигаем элементы влево
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.size - 1] = None
        self.size -= 1
        
        return removed_value
    
    def find(self, value):
        """
        Поиск элемента по значению.
        Трудоемкость: O(n) - последовательный перебор.
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def get(self, index):
        """Получение элемента по индексу. O(1)"""
        if index < 0 or index >= self.size:
            raise IndexError(f"Индекс {index} выходит за границы [0, {self.size - 1}]")
        return self.data[index]
    
    def __str__(self):
        """Строковое представление массива."""
        if self.size > 10:
            return f"DynamicArray([{', '.join(map(str, self.data[:5]))} ... {', '.join(map(str, self.data[self.size-5:self.size]))}], size={self.size}, capacity={self.capacity})"
        return f"DynamicArray({self.data[:self.size]}, size={self.size}, capacity={self.capacity})"


def benchmark_static_vs_dynamic():
    """
    Сравнение производительности статического и динамического массивов.
    """
    N = 100000
    
    print("\n=== Сравнение производительности ===\n")
    
    # Тест динамического массива
    print(f"1. Динамический массив - вставка {N} элементов:")
    dynamic_arr = DynamicArray(initial_capacity=8)
    
    start_time = time.time()
    for i in range(N):
        dynamic_arr.pushBack(i)
    end_time = time.time()
    
    dynamic_time = end_time - start_time
    print(f"   Время выполнения: {dynamic_time:.4f} секунд")
    print(f"   Количество расширений: {dynamic_arr.resize_count}")
    print(f"   Финальная вместимость: {dynamic_arr.capacity}")
    print(f"   Размер: {dynamic_arr.size}")
    
    # Тест статического массива (заранее выделенного)
    print(f"\n2. Статический массив (предварительно выделенный на {N} элементов):")
    static_data = [None] * N
    
    start_time = time.time()
    for i in range(N):
        static_data[i] = i
    end_time = time.time()
    
    static_time = end_time - start_time
    print(f"   Время выполнения: {static_time:.4f} секунд")
    
    # Тест статического массива с недостаточной вместимостью
    print(f"\n3. Статический массив (недостаточная вместимость - 1000 элементов):")
    print(f"   Попытка вставить {N} элементов...")
    try:
        from zadanie_01_static_array import StaticArray
        small_static = StaticArray(1000)
        
        start_time = time.time()
        for i in range(N):
            small_static.pushBack(i)
        end_time = time.time()
        
        print(f"   Время выполнения: {end_time - start_time:.4f} секунд")
    except OverflowError as e:
        print(f"   Ошибка: переполнение массива после вставки 1000 элементов")
        print(f"   Невозможно вставить все {N} элементов в статический массив")
    
    # Анализ
    print("\n=== Анализ результатов ===")
    print(f"Динамический массив: {dynamic_time:.4f} сек")
    print(f"Статический массив:  {static_time:.4f} сек")
    
    if dynamic_time > 0 and static_time > 0:
        ratio = dynamic_time / static_time
        print(f"Отношение времен:    {ratio:.2f}x")
    
    print("\nВыводы:")
    print("- Динамический массив немного медленнее из-за расширений")
    print(f"- Произошло всего {dynamic_arr.resize_count} расширений для {N} элементов")
    print("- Амортизированная сложность pushBack остается O(1)")
    print("- Статический массив требует заранее знать размер данных")
    print("- При превышении размера статического массива происходит ошибка")


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование динамического массива ===\n")
    
    # Базовые операции
    print("1. Создание динамического массива с начальной вместимостью 4:")
    arr = DynamicArray(initial_capacity=4)
    print(f"   {arr}")
    
    print("\n2. Добавление элементов (следим за расширениями):")
    for i in range(10):
        arr.pushBack(i * 10)
    print(f"   {arr}")
    
    print("\n3. Вставка элемента в начало:")
    arr.pushFront(999)
    print(f"   {arr}")
    
    print("\n4. Вставка элемента на позицию 5:")
    arr.insert(5, 777)
    print(f"   {arr}")
    
    print("\n5. Поиск элемента 50:")
    index = arr.find(50)
    print(f"   Найден на позиции: {index}")
    
    print("\n6. Удаление элемента на позиции 3:")
    removed = arr.remove(3)
    print(f"   Удален: {removed}")
    print(f"   {arr}")
    
    # Бенчмарк
    benchmark_static_vs_dynamic()
    
    print("\n=== Преимущества динамического массива ===")
    print("✓ Автоматическое управление памятью")
    print("✓ Не требует заранее знать размер данных")
    print("✓ Амортизированная сложность O(1) для pushBack")
    print("✓ Эффективная стратегия расширения ×2")
    print("✓ Предотвращает переполнение")
