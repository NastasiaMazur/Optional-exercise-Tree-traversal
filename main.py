# Optional exercise: Tree traversal #

# Part 1

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def traverse_in_order(self, visitor):
        if self.left:
            self.left.traverse_in_order(visitor)
        visitor(self)
        if self.right:
            self.right.traverse_in_order(visitor)

    def traverse_pre_order(self, visitor):
        visitor(self)
        if self.left:
            self.left.traverse_pre_order(visitor)
        if self.right:
            self.right.traverse_pre_order(visitor)

    def traverse_post_order(self, visitor):
        if self.left:
            self.left.traverse_post_order(visitor)
        if self.right:
            self.right.traverse_post_order(visitor)
        visitor(self)

def visit(node):
    print(f"Visiting {node.value}")

#My tree:
root = TreeNode("+")
root.left = TreeNode("*")
root.left.left = TreeNode("A")
root.left.right = TreeNode("-")
root.left.right.left = TreeNode("B")
root.left.right.right = TreeNode("C")

root.right = TreeNode("+")
root.right.left = TreeNode("D")
root.right.right = TreeNode("E")

print("Recursive In-Order Traversal:")
root.traverse_in_order(visit)


print("\nRecursive Pre-Order Traversal:")
root.traverse_pre_order(visit)

print("\nRecursive Post-Order Traversal:")
root.traverse_post_order(visit)

# Part 2 (Recursive only)
