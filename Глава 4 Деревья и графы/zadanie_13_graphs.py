"""
Задание 13. Графы
Хранение графов: матрица смежности, список смежности.
Реализовать алгоритмы: BFS, DFS, поиск кратчайшего пути в невзвешенном графе (BFS).
"""

from collections import deque


class GraphAdjMatrix:
    """Граф на основе матрицы смежности."""
    
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, directed=False):
        """Добавление ребра."""
        self.matrix[u][v] = 1
        if not directed:
            self.matrix[v][u] = 1
    
    def display(self):
        print("\nМатрица смежности:")
        for row in self.matrix:
            print("  ", row)


class GraphAdjList:
    """Граф на основе списка смежности."""
    
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}
    
    def add_edge(self, u, v, directed=False):
        """Добавление ребра."""
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)
    
    def bfs(self, start):
        """Поиск в ширину. O(V + E)."""
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Поиск в глубину. O(V + E)."""
        visited = [False] * self.num_vertices
        result = []
        
        def dfs_recursive(v):
            visited[v] = True
            result.append(v)
            
            for neighbor in self.adj_list[v]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def shortest_path(self, start, end):
        """Кратчайший путь в невзвешенном графе (BFS)."""
        visited = [False] * self.num_vertices
        parent = [-1] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        
        while queue:
            vertex = queue.popleft()
            
            if vertex == end:
                # Восстановление пути
                path = []
                current = end
                while current != -1:
                    path.append(current)
                    current = parent[current]
                return path[::-1]
            
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = vertex
                    queue.append(neighbor)
        
        return None  # Путь не найден
    
    def display(self):
        print("\nСписок смежности:")
        for vertex, neighbors in self.adj_list.items():
            print(f"  {vertex}: {neighbors}")


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          ГРАФЫ")
    print("="*60)
    
    # Граф с 6 вершинами
    g = GraphAdjList(6)
    
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]
    
    print("\n1. Создание графа (неориентированного):")
    print("   Ребра:", edges)
    
    for u, v in edges:
        g.add_edge(u, v)
    
    g.display()
    
    print("\n2. Обход в ширину (BFS) из вершины 0:")
    bfs_result = g.bfs(0)
    print(f"   Порядок: {bfs_result}")
    
    print("\n3. Обход в глубину (DFS) из вершины 0:")
    dfs_result = g.dfs(0)
    print(f"   Порядок: {dfs_result}")
    
    print("\n4. Кратчайший путь от 0 до 5:")
    path = g.shortest_path(0, 5)
    print(f"   Путь: {' -> '.join(map(str, path))}")
    
    print("\n5. Сравнение матрицы и списка смежности:")
    gm = GraphAdjMatrix(6)
    for u, v in edges:
        gm.add_edge(u, v)
    gm.display()
