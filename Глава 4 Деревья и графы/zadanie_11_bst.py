"""
Задание 11. Бинарное дерево поиска (BST)
Реализовать: вставку, поиск, удаление, обходы (in-order, pre-order, post-order).
Проверить, является ли дерево сбалансированным.
"""


class TreeNode:
    """Узел бинарного дерева."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """Бинарное дерево поиска."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Вставка элемента. O(h), где h - высота дерева."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Поиск элемента. O(h)."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Удаление элемента. O(h)."""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Узел найден
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Узел с двумя детьми: находим минимум в правом поддереве
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def inorder(self):
        """Симметричный обход (возрастающий порядок)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder(self):
        """Прямой обход."""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self):
        """Обратный обход."""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def is_balanced(self):
        """Проверка сбалансированности дерева."""
        return self._check_balance(self.root)[0]
    
    def _check_balance(self, node):
        """Возвращает (is_balanced, height)."""
        if node is None:
            return True, 0
        
        left_balanced, left_height = self._check_balance(node.left)
        right_balanced, right_height = self._check_balance(node.right)
        
        balanced = (left_balanced and right_balanced and 
                   abs(left_height - right_height) <= 1)
        height = max(left_height, right_height) + 1
        
        return balanced, height


# Тестирование
if __name__ == "__main__":
    print("="*60)
    print("          БИНАРНОЕ ДЕРЕВО ПОИСКА")
    print("="*60)
    
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    print("\n1. Вставка элементов:", values)
    for val in values:
        bst.insert(val)
    
    print("\n2. Обходы дерева:")
    print(f"   In-order:   {bst.inorder()}")
    print(f"   Pre-order:  {bst.preorder()}")
    print(f"   Post-order: {bst.postorder()}")
    
    print("\n3. Поиск элементов:")
    for val in [40, 90]:
        found = bst.search(val)
        print(f"   {val}: {'✓ найден' if found else '✗ не найден'}")
    
    print("\n4. Удаление элемента 30:")
    bst.delete(30)
    print(f"   In-order после удаления: {bst.inorder()}")
    
    print("\n5. Проверка сбалансированности:")
    print(f"   Дерево сбалансировано: {bst.is_balanced()}")
    
    # Несбалансированное дерево
    print("\n6. Создание несбалансированного дерева:")
    unbalanced = BST()
    for i in range(1, 6):
        unbalanced.insert(i)
    print(f"   Элементы: {list(range(1, 6))}")
    print(f"   In-order: {unbalanced.inorder()}")
    print(f"   Сбалансировано: {unbalanced.is_balanced()}")
