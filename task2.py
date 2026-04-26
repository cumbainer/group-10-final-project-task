# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до
# двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги,
# щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною
# кількістю символів, а також бути нечутливою до регістру та пробілів.
from typing import Any, Union


class Node:
    def __init__(self, data: Union[Any, None] = None, prev: Union['Node', None] = None,
                 next: Union['Node', None] = None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_end(self, data):
        new_node = Node(data)
        last = self.tail.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.tail
        self.tail.prev = new_node

    def get_first(self):
        if self.head.next is self.tail:
            return None
        return self.head.next

    def get_last(self):
        if self.tail.prev is self.head:
            return None
        return self.tail.prev

    def delete_first(self):
        if self.head.next is self.tail:
            return None

        first = self.head.next
        self.head.next = first.next
        first.next.prev = self.head

        return first.data

    def delete_last(self):
        if self.tail.prev is self.head:
            return None

        last = self.tail.prev
        self.tail.prev = last.prev
        last.prev.next = self.tail
        return last.data


# deque implemented with doubly linked lists just for practice
class Deque:
    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def enqueue(self, data: Any):
        self.linked_list.insert_end(data)

    def peek_start(self) -> Any:
        return self.linked_list.get_first().data

    def peek_end(self) -> Any:
        return self.linked_list.get_last().data

    def pop_start(self):
        return self.linked_list.delete_first()

    def pop_end(self):
        return self.linked_list.delete_last()

    def size(self) -> int:
        def get_size(node, n=0):
            if node is self.linked_list.tail:
                return n
            return get_size(node.next, n + 1)

        return get_size(self.linked_list.head.next)

    def clear(self):
        while self.size() > 0:
            self.pop_start()


class Program:
    def __init__(self):
        self.deque = Deque()

    def is_palindrome(self, word: str):
        word = word.lower().replace(" ", "")
        for char in word:
            self.deque.enqueue(char)
        while self.deque.size() > 1:
            start_char: str = self.deque.peek_start()
            end_char: str = self.deque.peek_end()
            if start_char == end_char:
                self.deque.pop_start()
                self.deque.pop_end()
            else:
                self.deque.clear()
                return False

        self.deque.clear()
        return True

def main():
     program = Program()
     not_palindrome = "palindrome"
     palindrome1 = "RacEcar"
     palindrome2 = "LevEl"
     print(f"Word {not_palindrome} is NOT palindrome: {program.is_palindrome(not_palindrome)}")
     print(f"Word {palindrome1} is palindrome: {program.is_palindrome(palindrome1)}")
     print(f"Word {palindrome2} is palindrome: {program.is_palindrome(palindrome2)}")

if __name__ == '__main__':
    main()