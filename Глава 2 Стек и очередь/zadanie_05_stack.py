"""
Задание 5. Стек
Реализовать стек на:
- массиве,
- связном списке.
Используя стек, проверить корректность скобочной последовательности.
"""


class StackArray:
    """Стек на основе массива (списка Python)."""
    
    def __init__(self):
        self.data = []
    
    def push(self, value):
        """
        Добавление элемента на вершину стека.
        Трудоемкость: O(1) амортизированная.
        """
        self.data.append(value)
    
    def pop(self):
        """
        Удаление и возврат элемента с вершины стека.
        Трудоемкость: O(1).
        
        Raises:
            IndexError: если стек пуст
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        return self.data.pop()
    
    def peek(self):
        """
        Просмотр элемента на вершине стека без удаления.
        Трудоемкость: O(1).
        
        Raises:
            IndexError: если стек пуст
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        return self.data[-1]
    
    def isEmpty(self):
        """Проверка, пуст ли стек. O(1)"""
        return len(self.data) == 0
    
    def size(self):
        """Получение размера стека. O(1)"""
        return len(self.data)
    
    def __str__(self):
        return f"StackArray({self.data})"


class Node:
    """Узел для связного списка."""
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    """Стек на основе связного списка."""
    
    def __init__(self):
        self.head = None
        self._size = 0
    
    def push(self, value):
        """
        Добавление элемента на вершину стека.
        Трудоемкость: O(1).
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def pop(self):
        """
        Удаление и возврат элемента с вершины стека.
        Трудоемкость: O(1).
        
        Raises:
            IndexError: если стек пуст
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        
        value = self.head.data
        self.head = self.head.next
        self._size -= 1
        return value
    
    def peek(self):
        """
        Просмотр элемента на вершине стека без удаления.
        Трудоемкость: O(1).
        
        Raises:
            IndexError: если стек пуст
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        return self.head.data
    
    def isEmpty(self):
        """Проверка, пуст ли стек. O(1)"""
        return self.head is None
    
    def size(self):
        """Получение размера стека. O(1)"""
        return self._size
    
    def toList(self):
        """Преобразование в список для отображения."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self):
        return f"StackLinkedList({self.toList()})"


def isBalancedParentheses(expression):
    """
    Проверка корректности скобочной последовательности.
    Трудоемкость: O(n), где n - длина строки.
    
    Args:
        expression: строка со скобками
    
    Returns:
        True, если последовательность корректна, иначе False
    """
    stack = StackArray()
    
    # Соответствие открывающих и закрывающих скобок
    matching = {')': '(', ']': '[', '}': '{'}
    opening = set('([{')
    closing = set(')]}')
    
    for char in expression:
        if char in opening:
            # Открывающая скобка - кладем в стек
            stack.push(char)
        elif char in closing:
            # Закрывающая скобка
            if stack.isEmpty():
                # Нет соответствующей открывающей скобки
                return False
            
            last_opening = stack.pop()
            if last_opening != matching[char]:
                # Типы скобок не совпадают
                return False
    
    # В конце стек должен быть пуст
    return stack.isEmpty()


def checkParenthesesDetailed(expression):
    """
    Подробная проверка скобочной последовательности с объяснением.
    
    Args:
        expression: строка со скобками
    
    Returns:
        Кортеж (результат, сообщение)
    """
    stack = StackArray()
    matching = {')': '(', ']': '[', '}': '{'}
    opening = set('([{')
    closing = set(')]}')
    
    for i, char in enumerate(expression):
        if char in opening:
            stack.push((char, i))
        elif char in closing:
            if stack.isEmpty():
                return False, f"Ошибка на позиции {i}: закрывающая скобка '{char}' без соответствующей открывающей"
            
            last_opening, pos = stack.pop()
            if last_opening != matching[char]:
                return False, f"Ошибка на позиции {i}: ожидалась '{matching[char]}', но найдена '{last_opening}' на позиции {pos}"
    
    if not stack.isEmpty():
        char, pos = stack.peek()
        return False, f"Ошибка: незакрытая скобка '{char}' на позиции {pos}"
    
    return True, "Скобочная последовательность корректна"


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование стека на массиве ===\n")
    
    stack_arr = StackArray()
    
    print("1. Добавление элементов в стек:")
    for i in [10, 20, 30, 40, 50]:
        stack_arr.push(i)
        print(f"   push({i}): {stack_arr}")
    
    print("\n2. Просмотр вершины стека:")
    print(f"   peek(): {stack_arr.peek()}")
    print(f"   Стек: {stack_arr}")
    
    print("\n3. Извлечение элементов:")
    while not stack_arr.isEmpty():
        value = stack_arr.pop()
        print(f"   pop(): {value}, осталось: {stack_arr}")
    
    print("\n=== Тестирование стека на связном списке ===\n")
    
    stack_ll = StackLinkedList()
    
    print("1. Добавление элементов в стек:")
    for i in ['A', 'B', 'C', 'D', 'E']:
        stack_ll.push(i)
        print(f"   push('{i}'): {stack_ll}")
    
    print("\n2. Просмотр вершины стека:")
    print(f"   peek(): {stack_ll.peek()}")
    print(f"   Размер: {stack_ll.size()}")
    
    print("\n3. Извлечение 2 элементов:")
    for _ in range(2):
        value = stack_ll.pop()
        print(f"   pop(): {value}, осталось: {stack_ll}")
    
    print("\n=== Проверка скобочной последовательности ===\n")
    
    test_cases = [
        "()",
        "(())",
        "()()",
        "((()))",
        "()[]{}",
        "{[()]}",
        "(()",
        "())",
        "([)]",
        "{[(])}",
        "",
        "((([[[{{{",
        "}}}}]]]]))))",
        "{[}]",
        "(a + b) * [c - d]",
        "function(array[index])",
    ]
    
    print("Тестирование различных последовательностей:\n")
    for expr in test_cases:
        result = isBalancedParentheses(expr)
        status = "✓ КОРРЕКТНА" if result else "✗ НЕКОРРЕКТНА"
        print(f"   '{expr:30}' => {status}")
    
    print("\n=== Подробная проверка с объяснением ошибок ===\n")
    
    detailed_tests = [
        "(())",
        "(()",
        "())",
        "([)]",
        "{[(])}",
        "((([[[{{{",
    ]
    
    for expr in detailed_tests:
        result, message = checkParenthesesDetailed(expr)
        print(f"Выражение: '{expr}'")
        print(f"  {message}\n")
    
    print("=== Сравнение реализаций стека ===")
    print("\nСтек на массиве:")
    print("  ✓ Простая реализация")
    print("  ✓ Хорошая локальность данных (кэш процессора)")
    print("  ✓ Меньше накладных расходов памяти")
    print("  ~ Может потребоваться расширение массива")
    
    print("\nСтек на связном списке:")
    print("  ✓ Неограниченный размер")
    print("  ✓ Не требуется расширение")
    print("  ✗ Дополнительная память на ссылки")
    print("  ✗ Хуже локальность данных")
    
    print("\n=== Применение стека ===")
    print("• Проверка скобочных последовательностей")
    print("• Вычисление арифметических выражений")
    print("• Обход дерева в глубину (DFS)")
    print("• История операций (Undo/Redo)")
    print("• Обратная польская нотация")
    print("• Рекурсия (call stack)")
