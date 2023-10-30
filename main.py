# Optional exercise: Tree traversal #

# Part 1
print('PART 1')
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def visit(node):
    print(node.value, end=', ')

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


# Construct the tree


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

# Part 2 (Recursive only)

print('\n\n''PART 2')

def traverse_in_order(node, visitor):
    if node is not None:
        traverse_in_order(node.left, visitor)
        visitor(node)
        traverse_in_order(node.right, visitor)


def traverse_pre_order(node, visitor):
    if node is not None:
        visitor(node)
        traverse_pre_order(node.left, visitor)
        traverse_pre_order(node.right, visitor)


def traverse_post_order(node, visitor):
    if node is not None:
        traverse_post_order(node.left, visitor)
        traverse_post_order(node.right, visitor)
        visitor(node)


print("In-order: ", end='')
traverse_in_order(root, visit)

print("\nPre-order: ", end='')
traverse_pre_order(root, visit)

print("\nPost-order: ", end='')
traverse_post_order(root, visit)