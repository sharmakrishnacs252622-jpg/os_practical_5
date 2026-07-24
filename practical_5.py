import time
import os
from colorama import Fore, Style, init

init(autoreset=True)


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
            print(Fore.RED + "Queue is full. Cannot enqueue.")
        else:
            self.queue.append(item)
            print(Fore.GREEN + f"Enqueued: {item}")
            time.sleep(0.5)

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(Fore.YELLOW + f"Dequeued: {item}")
        time.sleep(0.5)
        return item

    def peek(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
            return None
        print(Fore.BLUE + f"Front of the queue: {self.queue[0]}")
        return self.queue[0]

    def traverse(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            for item in self.queue:
                print(Fore.CYAN + str(item), end=" ", flush=True)
                time.sleep(0.2)
            print()
        time.sleep(0.5)

    def display_list(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            print(Fore.BLUE + "Current Queue List:")
            for index, item in enumerate(self.queue):
                print(Fore.BLUE + f"{index + 1}. {item}")
                time.sleep(0.2)
        time.sleep(0.5)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    max_size = int(input(Fore.YELLOW + "Enter the maximum size of the queue: "))
    q = Queue(max_size)

    while True:
        clear_screen()
        print(Fore.MAGENTA + "Queue Operation Menu")
        print(Fore.MAGENTA + "1. Enqueue")
        print(Fore.MAGENTA + "2. Dequeue")
        print(Fore.MAGENTA + "3. Peek")
        print(Fore.MAGENTA + "4. Traverse")
        print(Fore.MAGENTA + "5. Display List")
        print(Fore.MAGENTA + "6. Check if Queue is Empty")
        print(Fore.MAGENTA + "7. Check if Queue is Full")
        print(Fore.MAGENTA + "8. Exit")

        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == '1':
            item = input(Fore.YELLOW + "Enter the item to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.peek()
        elif choice == '4':
            q.traverse()
        elif choice == '5':
            q.display_list()
        elif choice == '6':
            if q.is_empty():
                print(Fore.RED + "Queue is empty.")
            else:
                print(Fore.GREEN + "Queue is not empty.")
        elif choice == '7':
            if q.is_full():
                print(Fore.RED + "Queue is full.")
            else:
                print(Fore.GREEN + "Queue is not full.")
        elif choice == '8':
            break
        else:
            print(Fore.RED + "Invalid choice! Please try again.")

        input(Fore.GREEN + "Press Enter to continue...")

    clear_screen()
    print(Fore.MAGENTA + "Exiting the program. Goodbye!")
