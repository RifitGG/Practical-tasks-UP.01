"""
Задание 1. Статический массив
Реализовать функции: pushBack, pushFront, insert(index, value), remove(index), find(value).
Оценить трудоемкость каждой операции (в комментариях).
"""


class StaticArray:
    def __init__(self, capacity):
        """
        Инициализация статического массива с фиксированной ёмкостью.
        
        Args:
            capacity: максимальная вместимость массива
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def pushBack(self, value):
        """
        Добавление элемента в конец массива.
        Трудоемкость: O(1) - простое присваивание по индексу.
        
        Args:
            value: значение для добавления
        
        Raises:
            OverflowError: если массив заполнен
        """
        if self.size >= self.capacity:
            raise OverflowError("Массив заполнен, невозможно добавить элемент")
        
        self.data[self.size] = value
        self.size += 1
    
    def pushFront(self, value):
        """
        Добавление элемента в начало массива.
        Трудоемкость: O(n) - требуется сдвинуть все существующие элементы вправо.
        
        Args:
            value: значение для добавления
        
        Raises:
            OverflowError: если массив заполнен
        """
        if self.size >= self.capacity:
            raise OverflowError("Массив заполнен, невозможно добавить элемент")
        
        # Сдвигаем все элементы вправо
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[0] = value
        self.size += 1
    
    def insert(self, index, value):
        """
        Вставка элемента на произвольную позицию.
        Трудоемкость: O(n) - требуется сдвинуть элементы справа от позиции вставки.
        
        Args:
            index: индекс для вставки
            value: значение для добавления
        
        Raises:
            OverflowError: если массив заполнен
            IndexError: если индекс выходит за границы
        """
        if self.size >= self.capacity:
            raise OverflowError("Массив заполнен, невозможно добавить элемент")
        
        if index < 0 or index > self.size:
            raise IndexError(f"Индекс {index} выходит за границы [0, {self.size}]")
        
        # Сдвигаем элементы вправо от позиции вставки
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, index):
        """
        Удаление элемента по индексу.
        Трудоемкость: O(n) - требуется сдвинуть все элементы слева от удаленного.
        
        Args:
            index: индекс элемента для удаления
        
        Returns:
            Удаленное значение
        
        Raises:
            IndexError: если индекс выходит за границы
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
        Трудоемкость: O(n) - требуется последовательный перебор всех элементов.
        
        Args:
            value: значение для поиска
        
        Returns:
            Индекс первого найденного элемента или -1, если не найден
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def get(self, index):
        """
        Получение элемента по индексу.
        Трудоемкость: O(1) - прямой доступ по индексу.
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Индекс {index} выходит за границы [0, {self.size - 1}]")
        return self.data[index]
    
    def __str__(self):
        """Строковое представление массива."""
        return f"StaticArray({self.data[:self.size]})"
    
    def __repr__(self):
        return self.__str__()


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование статического массива ===\n")
    
    # Создаем массив вместимостью 10
    arr = StaticArray(10)
    
    # Тест pushBack
    print("1. Добавление элементов в конец (pushBack):")
    for i in range(5):
        arr.pushBack(i * 10)
    print(f"   Массив: {arr}")
    
    # Тест pushFront
    print("\n2. Добавление элемента в начало (pushFront):")
    arr.pushFront(100)
    print(f"   Массив: {arr}")
    
    # Тест insert
    print("\n3. Вставка элемента на позицию 3:")
    arr.insert(3, 999)
    print(f"   Массив: {arr}")
    
    # Тест find
    print("\n4. Поиск элемента со значением 20:")
    index = arr.find(20)
    print(f"   Найден на позиции: {index}")
    
    # Тест remove
    print("\n5. Удаление элемента на позиции 2:")
    removed = arr.remove(2)
    print(f"   Удален элемент: {removed}")
    print(f"   Массив: {arr}")
    
    # Тест переполнения
    print("\n6. Тест переполнения массива:")
    try:
        for i in range(10):
            arr.pushBack(i)
    except OverflowError as e:
        print(f"   Ошибка: {e}")
        print(f"   Размер массива: {arr.size}/{arr.capacity}")
    
    # Тест поиска несуществующего элемента
    print("\n7. Поиск несуществующего элемента (777):")
    index = arr.find(777)
    print(f"   Результат: {index} (не найден)")
    
    print("\n=== Анализ трудоемкости ===")
    print("pushBack:    O(1) - добавление в конец")
    print("pushFront:   O(n) - сдвиг всех элементов")
    print("insert:      O(n) - сдвиг части элементов")
    print("remove:      O(n) - сдвиг части элементов")
    print("find:        O(n) - последовательный поиск")
