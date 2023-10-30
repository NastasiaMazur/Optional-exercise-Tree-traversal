# Optional exercise: Tree traversal #

# Part 1

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def visit(node):
    print(f"Visiting {node.value}")

def traverse_recursively_in_order(node):
    if node is not None:
        traverse_recursively_in_order(node.left)
        visit(node)
        traverse_recursively_in_order(node.right)


def traverse_in_order_imperatively(node):
    stack = []
    current = node

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            visit(current)
            current = current.right

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
traverse_recursively_in_order(root)

print("\nImperative In-Order Traversal:")
traverse_in_order_imperatively(root)
