"""
Задание 7. Задача "Калькулятор"
Считать выражение в инфиксной форме.
Используя стек, преобразовать в обратную польскую нотацию (ОПН).
Вычислить результат.
"""


def infixToPostfix(expression):
    """
    Преобразование инфиксного выражения в постфиксное (ОПН).
    Использует алгоритм Дейкстры (Shunting Yard).
    Трудоемкость: O(n), где n - длина выражения.
    
    Args:
        expression: строка с инфиксным выражением (например, "3 + 4 * 2")
    
    Returns:
        Список токенов в постфиксной нотации
    """
    # Приоритеты операторов
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Правая ассоциативность (для степени)
    right_associative = {'^'}
    
    output = []  # Выходная очередь (результат в ОПН)
    stack = []   # Стек операторов
    
    # Токенизация: разбиваем строку на числа, операторы и скобки
    tokens = tokenize(expression)
    
    for token in tokens:
        if isNumber(token):
            # Число - сразу в выход
            output.append(token)
        
        elif token in precedence:
            # Оператор
            while (stack and 
                   stack[-1] != '(' and 
                   stack[-1] in precedence and
                   (precedence[stack[-1]] > precedence[token] or 
                    (precedence[stack[-1]] == precedence[token] and 
                     token not in right_associative))):
                output.append(stack.pop())
            
            stack.append(token)
        
        elif token == '(':
            # Открывающая скобка - в стек
            stack.append(token)
        
        elif token == ')':
            # Закрывающая скобка - выталкиваем до открывающей
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            
            if not stack:
                raise ValueError("Несбалансированные скобки")
            
            stack.pop()  # Удаляем '('
    
    # Выталкиваем оставшиеся операторы
    while stack:
        if stack[-1] in '()':
            raise ValueError("Несбалансированные скобки")
        output.append(stack.pop())
    
    return output


def tokenize(expression):
    """
    Разбивает строку на токены (числа, операторы, скобки).
    
    Args:
        expression: строка с выражением
    
    Returns:
        Список токенов
    """
    tokens = []
    current_number = ""
    
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        else:
            if current_number:
                tokens.append(current_number)
                current_number = ""
            
            if char in '+-*/^()':
                tokens.append(char)
            # Пропускаем пробелы и другие символы
    
    if current_number:
        tokens.append(current_number)
    
    return tokens


def isNumber(token):
    """Проверка, является ли токен числом."""
    try:
        float(token)
        return True
    except ValueError:
        return False


def evaluatePostfix(postfix):
    """
    Вычисление значения выражения в обратной польской нотации.
    Трудоемкость: O(n), где n - количество токенов.
    
    Args:
        postfix: список токенов в постфиксной нотации
    
    Returns:
        Результат вычисления
    """
    stack = []
    
    for token in postfix:
        if isNumber(token):
            # Число - кладем в стек
            stack.append(float(token))
        else:
            # Оператор - извлекаем два операнда
            if len(stack) < 2:
                raise ValueError(f"Недостаточно операндов для оператора '{token}'")
            
            b = stack.pop()
            a = stack.pop()
            
            # Выполняем операцию
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = a / b
            elif token == '^':
                result = a ** b
            else:
                raise ValueError(f"Неизвестный оператор: '{token}'")
            
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Некорректное выражение")
    
    return stack[0]


def calculate(expression):
    """
    Вычисление значения инфиксного выражения.
    
    Args:
        expression: строка с инфиксным выражением
    
    Returns:
        Результат вычисления
    """
    postfix = infixToPostfix(expression)
    return evaluatePostfix(postfix)


def printCalculationSteps(expression):
    """
    Вывод пошагового процесса вычисления.
    """
    print(f"\nВыражение: {expression}")
    print("-" * 60)
    
    # Преобразование в ОПН
    print("\n1. Преобразование в обратную польскую нотацию:")
    tokens = tokenize(expression)
    print(f"   Токены: {tokens}")
    
    postfix = infixToPostfix(expression)
    print(f"   ОПН:    {' '.join(postfix)}")
    
    # Вычисление
    print("\n2. Вычисление ОПН:")
    stack = []
    
    for token in postfix:
        if isNumber(token):
            stack.append(float(token))
            print(f"   Число {token:5} -> Стек: {stack}")
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
                op_str = f"{a} + {b} = {result}"
            elif token == '-':
                result = a - b
                op_str = f"{a} - {b} = {result}"
            elif token == '*':
                result = a * b
                op_str = f"{a} * {b} = {result}"
            elif token == '/':
                result = a / b
                op_str = f"{a} / {b} = {result}"
            elif token == '^':
                result = a ** b
                op_str = f"{a} ^ {b} = {result}"
            
            stack.append(result)
            print(f"   Оператор {token}: {op_str} -> Стек: {stack}")
    
    result = stack[0]
    print(f"\n3. Результат: {result}")
    print("=" * 60)
    
    return result


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("           КАЛЬКУЛЯТОР С ОБРАТНОЙ ПОЛЬСКОЙ НОТАЦИЕЙ")
    print("="*60)
    
    # Простые примеры
    test_expressions = [
        "3 + 4",
        "5 - 2",
        "6 * 7",
        "20 / 4",
        "2 + 3 * 4",
        "2 * 3 + 4",
        "(2 + 3) * 4",
        "2 * (3 + 4)",
        "2 + 3 * 4 - 5",
        "(2 + 3) * (4 - 1)",
        "10 + 2 * 6",
        "100 * 2 + 12",
        "100 * (2 + 12)",
        "100 * (2 + 12) / 14",
        "2 ^ 3",
        "2 ^ 3 ^ 2",
        "(2 ^ 3) ^ 2",
    ]
    
    print("\n=== Быстрые тесты ===\n")
    
    for expr in test_expressions:
        try:
            postfix = infixToPostfix(expr)
            result = evaluatePostfix(postfix)
            print(f"{expr:25} = {result:10.2f}  |  ОПН: {' '.join(postfix)}")
        except Exception as e:
            print(f"{expr:25} = ОШИБКА: {e}")
    
    # Подробные примеры с пошаговым выполнением
    print("\n" + "="*60)
    print("=== Подробное вычисление ===")
    
    detailed_examples = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 + 2 * 6 - 3",
        "(5 + 2) * (8 - 3)",
    ]
    
    for expr in detailed_examples:
        printCalculationSteps(expr)
    
    # Проверка ошибок
    print("\n" + "="*60)
    print("=== Тестирование обработки ошибок ===\n")
    
    error_cases = [
        ("2 + ", "Недостаточно операндов"),
        ("+ 2", "Недостаточно операндов"),
        ("2 +* 3", "Несколько операторов подряд"),
        ("(2 + 3", "Несбалансированные скобки"),
        ("2 + 3)", "Несбалансированные скобки"),
        ("10 / 0", "Деление на ноль"),
    ]
    
    for expr, expected_error in error_cases:
        try:
            result = calculate(expr)
            print(f"✗ '{expr}' => {result} (ожидалась ошибка: {expected_error})")
        except Exception as e:
            print(f"✓ '{expr}' => Ошибка: {e}")
    
    # Интерактивный режим (опционально)
    print("\n" + "="*60)
    print("=== Интерактивный калькулятор ===")
    print("Введите выражение (или 'q' для выхода):\n")
    
    # Примеры для пользователя
    print("Примеры выражений:")
    print("  2 + 3 * 4")
    print("  (5 + 3) * (2 - 1)")
    print("  10 / 2 + 3")
    print("  2 ^ 3 + 1")
    print()
    
    # Раскомментируйте для интерактивного режима:
    """
    while True:
        try:
            expr = input(">>> ").strip()
            
            if expr.lower() in ['q', 'quit', 'exit']:
                print("До свидания!")
                break
            
            if not expr:
                continue
            
            if expr == 'help':
                print("\nПоддерживаемые операторы: + - * / ^ ( )")
                print("Пример: (2 + 3) * 4\n")
                continue
            
            result = printCalculationSteps(expr)
            
        except KeyboardInterrupt:
            print("\n\nДо свидания!")
            break
        except Exception as e:
            print(f"Ошибка: {e}\n")
    """
    
    print("\n=== Преимущества обратной польской нотации ===")
    print("✓ Не требуются скобки")
    print("✓ Не требуется знание приоритетов операторов")
    print("✓ Простое вычисление с помощью стека")
    print("✓ Однозначность выражения")
    print("✓ Эффективная обработка: O(n)")
    
    print("\n=== Применение ===")
    print("• Вычисление арифметических выражений")
    print("• Калькуляторы и интерпретаторы")
    print("• Компиляторы (промежуточное представление)")
    print("• Процессоры с стековой архитектурой")
    print("• Язык программирования Forth")
