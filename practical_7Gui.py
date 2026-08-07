import tkinter as tk
from tkinter import messagebox, scrolledtext
import heapq
from collections import Counter

# ---------------- Huffman Node ---------------- #
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ---------------- Build Huffman Tree ---------------- #
def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


# ---------------- Generate Codes ---------------- #
def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix if prefix else "0"

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


# ---------------- Encoding ---------------- #
def huffman_encoding(data):
    if not data:
        return "", {}, {}

    frequencies = Counter(data)

    root = build_huffman_tree(frequencies)

    codebook = generate_codes(root)

    encoded_data = ''.join(codebook[ch] for ch in data)

    return encoded_data, codebook, frequencies


# ---------------- Decoding ---------------- #
def huffman_decoding(encoded_data, codebook):
    reverse = {v: k for k, v in codebook.items()}

    decoded = ""
    current = ""

    for bit in encoded_data:
        current += bit
        if current in reverse:
            decoded += reverse[current]
            current = ""

    return decoded


# ---------------- GUI Function ---------------- #
def run_huffman():

    text = entry.get()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text!")
        return

    encoded, codebook, freq = huffman_encoding(text)

    decoded = huffman_decoding(encoded, codebook)

    output.delete(1.0, tk.END)

    output.insert(tk.END, "========== HUFFMAN CODING ==========\n\n")

    output.insert(tk.END, "Original Text:\n")
    output.insert(tk.END, text + "\n\n")

    output.insert(tk.END, "Character Frequencies:\n")
    for k, v in freq.items():
        output.insert(tk.END, f"{repr(k)} : {v}\n")

    output.insert(tk.END, "\nCodebook:\n")
    for k, v in codebook.items():
        output.insert(tk.END, f"{repr(k)} : {v}\n")

    output.insert(tk.END, "\nEncoded Data:\n")
    output.insert(tk.END, encoded + "\n\n")

    output.insert(tk.END, "Decoded Data:\n")
    output.insert(tk.END, decoded + "\n\n")

    if text == decoded:
        output.insert(tk.END, "SUCCESS: Original and Decoded data MATCH.\n")
    else:
        output.insert(tk.END, "ERROR: Data does NOT Match.\n")


# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Huffman Coding GUI")
root.geometry("850x650")
root.configure(bg="#EAF4FC")

title = tk.Label(
    root,
    text="HUFFMAN CODING APPLICATION",
    font=("Arial", 20, "bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
title.pack(fill="x")

frame = tk.Frame(root, bg="#EAF4FC")
frame.pack(pady=20)

tk.Label(
    frame,
    text="Enter Text:",
    font=("Arial", 13, "bold"),
    bg="#EAF4FC"
).grid(row=0, column=0, padx=10)

entry = tk.Entry(frame, width=55, font=("Arial", 13))
entry.grid(row=0, column=1)

btn = tk.Button(
    root,
    text="Encode & Decode",
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    command=run_huffman
)
btn.pack(pady=10)

output = scrolledtext.ScrolledText(
    root,
    width=95,
    height=25,
    font=("Consolas", 11)
)
output.pack(pady=10)

footer = tk.Label(
    root,
    text="S110 KRISHNA SHARMA",
    font=("Arial", 12, "bold"),
    fg="blue",
    bg="#EAF4FC"
)
footer.pack(pady=8)

root.mainloop()
