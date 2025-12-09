"""
Задание 14. Задача "Острова"
Дан двумерный массив 0/1. Найти количество "островов" (компонент связности).
Использовать DFS или BFS.
"""


def count_islands_dfs(grid):
    """
    Подсчет островов с использованием DFS.
    Трудоемкость: O(m × n), где m и n - размеры сетки.
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    
    def dfs(i, j):
        """DFS для пометки всех ячеек текущего острова."""
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            visited[i][j] or grid[i][j] == 0):
            return
        
        visited[i][j] = True
        
        # Проверяем 4 соседние ячейки
        dfs(i - 1, j)  # вверх
        dfs(i + 1, j)  # вниз
        dfs(i, j - 1)  # влево
        dfs(i, j + 1)  # вправо
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    return count


def count_islands_bfs(grid):
    """Подсчет островов с использованием BFS."""
    if not grid or not grid[0]:
        return 0
    
    from collections import deque
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    
    def bfs(start_i, start_j):
        """BFS для пометки всех ячеек текущего острова."""
        queue = deque([(start_i, start_j)])
        visited[start_i][start_j] = True
        
        while queue:
            i, j = queue.popleft()
            
            # Проверяем 4 соседние ячейки
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                
                if (0 <= ni < rows and 0 <= nj < cols and 
                    not visited[ni][nj] and grid[ni][nj] == 1):
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    return count


def visualize_grid(grid):
    """Визуализация сетки."""
    print("\n  Сетка:")
    for row in grid:
        print("  ", ' '.join('■' if cell == 1 else '·' for cell in row))


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          ЗАДАЧА 'ОСТРОВА'")
    print("="*60)
    
    # Тестовые случаи
    test_cases = [
        {
            "name": "Простой случай - 1 остров",
            "grid": [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            "expected": 1
        },
        {
            "name": "Три острова",
            "grid": [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1]
            ],
            "expected": 3
        },
        {
            "name": "Один большой остров",
            "grid": [
                [1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            "expected": 1
        },
        {
            "name": "Диагональные острова (4 острова)",
            "grid": [
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1]
            ],
            "expected": 8
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"Тест {i}: {test['name']}")
        visualize_grid(test["grid"])
        
        result_dfs = count_islands_dfs(test["grid"])
        result_bfs = count_islands_bfs(test["grid"])
        
        print(f"\n  Результат DFS: {result_dfs} островов")
        print(f"  Результат BFS: {result_bfs} островов")
        print(f"  Ожидается:     {test['expected']} островов")
        
        if result_dfs == result_bfs == test["expected"]:
            print("  ✓ Тест пройден")
        else:
            print("  ✗ Тест провален")
