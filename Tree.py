class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = TreeNode(value)
        elif value > node.value:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = TreeNode(value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

tree.inorder_traversal(tree.root)
