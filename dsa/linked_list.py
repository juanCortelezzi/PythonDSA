from typing import Generic, Optional, TypeVar


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Optional[Node] = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.len = 0

    def __str__(self) -> str:
        return self.__rec_to_string(f"({self.len}) ", self.head)

    def __rec_to_string(self, s: str, node: Optional[Node[T]]):
        if node == None:
            return s + "null"
        return self.__rec_to_string(s + f"{node.value} <-> ", node.next)

    def push_front(self, value: T) -> None:
        node = Node(value)
        self.len += 1
        if self.head == None:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head = node

    def push_back(self, value: T) -> None:
        node = Node(value)
        self.len += 1
        if self.tail == None:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def pop_front(self) -> Optional[T]:
        if self.head == None:
            return None

        self.len -= 1
        node = self.head

        if self.head.next == None:
            self.head = self.tail = None
            return node.value

        self.head = self.head.next
        return node.value

    def pop_back(self) -> Optional[T]:
        if self.head == None:
            return None

        if self.head.next == None:
            node = self.head
            self.head = self.tail = None
            self.len -= 1
            return node.value

        secondToLast = self.head
        current = self.head.next

        while current.next != None:
            secondToLast = current
            current = current.next

        secondToLast.next = None
        self.tail = secondToLast
        self.len -= 1

        return current.value


if __name__ == "__main__":
    ll = LinkedList()
    ll.push_front(1)
    ll.push_front(2)
    ll.push_front(3)
    print(ll)
    ll.pop_back()
    print(ll)
    ll.pop_back()
    print(ll)
    ll.push_front(4)
    ll.push_back(5)
    print(ll)
    ll.pop_back()
    print(ll)
