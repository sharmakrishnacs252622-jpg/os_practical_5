import tkinter as tk
from tkinter import messagebox, simpledialog


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return False
        self.queue.append(item)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]


class QueueGUI:
    def __init__(self, root, max_size):
        self.q = Queue(max_size)
        self.root = root
        self.root.title("Queue Operations")
        self.root.geometry("350x420")

        tk.Label(root, text="Queue (GUI)", font=("Arial", 16, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(root, width=30, height=10)
        self.listbox.pack(pady=10)

        self.entry = tk.Entry(root, width=25)
        self.entry.pack(pady=5)

        tk.Button(root, text="Enqueue", width=20, command=self.enqueue_item).pack(pady=3)
        tk.Button(root, text="Dequeue", width=20, command=self.dequeue_item).pack(pady=3)
        tk.Button(root, text="Peek", width=20, command=self.peek_item).pack(pady=3)
        tk.Button(root, text="Check Empty", width=20, command=self.check_empty).pack(pady=3)
        tk.Button(root, text="Check Full", width=20, command=self.check_full).pack(pady=3)

        self.status = tk.Label(root, text="", fg="blue")
        self.status.pack(pady=10)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for item in self.q.queue:
            self.listbox.insert(tk.END, item)

    def enqueue_item(self):
        item = self.entry.get().strip()
        if not item:
            messagebox.showwarning("Input needed", "Please type something to enqueue.")
            return
        if self.q.enqueue(item):
            self.status.config(text=f"Enqueued: {item}")
            self.entry.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showerror("Full", "Queue is full. Cannot enqueue.")

    def dequeue_item(self):
        item = self.q.dequeue()
        if item is None:
            messagebox.showerror("Empty", "Queue is empty. Cannot dequeue.")
        else:
            self.status.config(text=f"Dequeued: {item}")
            self.refresh_list()

    def peek_item(self):
        item = self.q.peek()
        if item is None:
            messagebox.showinfo("Peek", "Queue is empty.")
        else:
            messagebox.showinfo("Peek", f"Front of queue: {item}")

    def check_empty(self):
        msg = "Queue is empty." if self.q.is_empty() else "Queue is not empty."
        self.status.config(text=msg)

    def check_full(self):
        msg = "Queue is full." if self.q.is_full() else "Queue is not full."
        self.status.config(text=msg)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    max_size = simpledialog.askinteger("Setup", "Enter maximum size of the queue:", minvalue=1)
    root.deiconify()
    app = QueueGUI(root, max_size)
    root.mainloop()
