import heapq

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def left_rotate(z):
    print(f"Left Rotation on {z.key}")

    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def right_rotate(z):
    print(f"Right Rotation on {z.key}")

    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(node, key):

    if node is None:
        print(f"Inserting {key}...")
        return AVLNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = 1 + max(height(node.left), height(node.right))

    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def heap_examples():
    arr = [9, 5, 6, 2, 3]

    min_heap = arr.copy()
    heapq.heapify(min_heap)

    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    max_heap = [-x for x in max_heap]

    print("\n=== Heap Examples ===")
    print("Min-Heap:", min_heap)
    print("Max-Heap:", max_heap)

print("=== AVL Tree Insertion and Balancing ===")

root = None

values = [20, 4, 15, 70, 50, 100, 80]

for value in values:
    root = insert(root, value)

print("\nAVL Tree Pre-Order Traversal:")
preorder(root)

print("\n")

heap_examples()

print("S110 KRISHNA SHARMA")
