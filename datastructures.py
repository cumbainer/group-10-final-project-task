from typing import Union, Any

#just for practice
class SinglyListNode:
    def __init__(self, data: Any, next: Union["SinglyListNode", None] = None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class SinglyLinkedList:
    def __init__(self, head_data: Any = None):
        self.head = SinglyListNode(data=head_data, next=None)

    def insert_after(self, prev_node: SinglyListNode, data) -> SinglyListNode:
        new_node = SinglyListNode(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        return self.head

    def delete_node(self, data: Any) -> SinglyListNode:
        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.data == data:
                prev.next = cur.next
                return self.head
            prev = cur
            cur = cur.next

        return self.head

    def insert_at_end(self, data: Any) -> SinglyListNode:
        cur_node = self.head
        while cur_node is not None:
            if cur_node.next is None:
                break
            cur_node = cur_node.next
        cur_node.next = SinglyListNode(data)
        return self.head

    def insert_at_start(self, data: Any) -> SinglyListNode:
        new_node = SinglyListNode(data)
        if self.head.next is not None:
            new_node.next = self.head.next
        self.head.next = new_node
        return self.head

    def search_element(self, data: Any) -> SinglyListNode | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        curr_node = self.head
        count = 0
        if curr_node is None:
            print("[]")
            return

        while True:
            print(f"{curr_node.data} --> ", end="")
            if curr_node.next is None:
                print("None", end="")
                return
            curr_node = curr_node.next
            count += 1

    def print_size(self):
        size = 0
        curr_node = self.head
        while curr_node is not None:
            if curr_node.next is None:
                print()
                print(f"Size: {size}")
            curr_node = curr_node.next
            size += 1
        if size == 0:
            print(f"Size: {0}")
