import tkinter as tk
from tkinter import scrolledtext
import heapq

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def __init__(self):
        self.output = []

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):

        self.output.append(f"Left Rotation on {z.key}")

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):

        self.output.append(f"Right Rotation on {z.key}")

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, node, key):

        if node is None:
            self.output.append(f"Inserting {key}...")
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.height(node.left),
                              self.height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def preorder(self, root):

        result = []

        def traverse(node):
            if node:
                result.append(str(node.key))
                traverse(node.left)
                traverse(node.right)

        traverse(root)

        return " ".join(result)

def run_demo():

    text.delete(1.0, tk.END)

    tree = AVLTree()
    root = None

    values = [20, 4, 15, 70, 50, 100, 80]

    text.insert(tk.END, "=== AVL Tree Insertion and Balancing ===\n\n")

    for value in values:
        root = tree.insert(root, value)

    for line in tree.output:
        text.insert(tk.END, line + "\n")

    text.insert(tk.END, "\nAVL Tree Pre-Order Traversal:\n")
    text.insert(tk.END, tree.preorder(root))

    text.insert(tk.END, "\n\n=== Heap Examples ===\n")

    arr = [9, 5, 6, 2, 3]

    min_heap = arr.copy()
    heapq.heapify(min_heap)

    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    max_heap = [-x for x in max_heap]

    text.insert(tk.END, f"Min-Heap: {min_heap}\n")
    text.insert(tk.END, f"Max-Heap: {max_heap}\n")

root = tk.Tk()
root.title("AVL Tree and Heap Demonstration")
root.geometry("800x650")
root.configure(bg="#E8F4FF")

title = tk.Label(
    root,
    text="AVL TREE INSERTION & HEAP DEMONSTRATION",
    font=("Arial", 18, "bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
title.pack(fill="x")

btn = tk.Button(
    root,
    text="Run Demo",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=run_demo
)
btn.pack(pady=15)

text = scrolledtext.ScrolledText(
    root,
    width=90,
    height=28,
    font=("Consolas", 11)
)
text.pack(padx=10, pady=10)

footer = tk.Label(
    root,
    text="S110 KRISHNA SHARMA",
    font=("Arial", 12, "bold"),
    fg="blue",
    bg="#E8F4FF"
)
footer.pack(pady=10)

root.mainloop()
