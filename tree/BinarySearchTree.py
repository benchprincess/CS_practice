class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                if node.right is None:
                    node.right = TreeNode(value)

    def is_bst(self):
        return self._is_bst_helper(self.root, float('-inf'), float('inf'))

    def _is_bst_helper(self, node, min_val, max_val):
        if node is None:
            return True

        if node.value <= min_val or node.value >= max_val:
            return False

        return (self._is_bst_helper(node.left, min_val, node.value) and self._is_bst_helper(node.right, node.value, max_val))


# 이진 검색 트리 만들기
bst = BinarySearchTree()

# 트리에 값 삽입
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# 트리가 이진 검색 트리인지 확인
print("Is the tree a valid Binary Search Tree? ", bst.is_bst())  # True

# 잘못된 이진 검색 트리 만들기 (잘못된 값 삽입)
bst_invalid = BinarySearchTree()
bst_invalid.insert(10)
bst_invalid.insert(5)
bst_invalid.insert(15)
bst_invalid.insert(3)
bst_invalid.insert(20)
bst_invalid.insert(7)

# 잘못된 트리가 이진 검색 트리인지 확인
print("Is the tree a valid Binary Search Tree? ", bst_invalid.is_bst())  # False
