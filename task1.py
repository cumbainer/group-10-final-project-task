# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові
# заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти
# з черги для "обробки", імітуючи таким чином роботу сервісного центру.
import time
from dataclasses import dataclass

from datastructures import SinglyLinkedList, SinglyListNode


# Implemented own queue using linked list just for practice. Note that it's not thread safe
#Doubly LinkedLists would be a better choice here, because I need to get last element
class Queue:
    def __init__(self):
        self.linked_list = SinglyLinkedList()

    def pop(self) -> Request:
        curr_node: SinglyListNode = self.linked_list.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        self.linked_list.delete_node(curr_node.data)
        return curr_node.data

    def enqueue(self, data: Request):
        self.linked_list.insert_at_end(data)


@dataclass
class Request:
    req_id: int


@dataclass
class Response:
    resp_id: int
    req: Request

    def __str__(self) -> str:
        return f"Response Id: {self.resp_id}. Linked req Id: {self.req.req_id}"


class RequestService:
    def __init__(self):
        self.request_queue = Queue()

    def generate_request(self, req_id: int) -> Request:
        req = Request(req_id)
        self.request_queue.enqueue(req)
        return req

    def process_request(self) -> Response:
        req: Request = self.request_queue.pop()
        print(f"Processing request with ID: {req.req_id}...")
        return Response(69420+req.req_id, req)


TOTAL_REQUESTS = 10


def main():
    req_service = RequestService()
    responses = []
    for req_number in range(1, TOTAL_REQUESTS):
        req_service.generate_request(req_number)
        req_service.request_queue.linked_list.print_list()
        print()
        resp = req_service.process_request()
        responses.append(resp)
        time.sleep(0.2)

    print(f"Is completed correctly: {TOTAL_REQUESTS == len(responses) + 1}")


if __name__ == '__main__':
    main()
