import unittest
from doubly_linked_list import DoublyLinkedList
from linked_list import LinkedList


class TestLL(unittest.TestCase):
    def test_dll_front(self):
        dll = LinkedList[int]()
        assert dll.len == 0
        dll.push_front(1)
        assert dll.len == 1
        dll.push_front(2)
        assert dll.len == 2

        assert dll.pop_front() == 2
        assert dll.len == 1
        assert dll.pop_front() == 1
        assert dll.len == 0

    def test_ddl_back(self):
        dll = LinkedList[int]()
        assert dll.len == 0
        dll.push_back(1)
        assert dll.len == 1
        dll.push_back(2)
        assert dll.len == 2

        assert dll.pop_back() == 2
        assert dll.len == 1
        assert dll.pop_back() == 1
        assert dll.len == 0

    def test_dll_front_back(self):
        dll = LinkedList[int]()
        assert dll.len == 0
        dll.push_front(1)
        assert dll.len == 1
        dll.push_back(2)
        assert dll.len == 2
        dll.push_front(3)
        assert dll.len == 3

        assert dll.pop_front() == 3
        assert dll.len == 2
        assert dll.pop_back() == 2
        assert dll.len == 1
        assert dll.pop_front() == 1
        assert dll.len == 0


class TestDLL(unittest.TestCase):
    def test_dll_front(self):
        dll = DoublyLinkedList[int]()
        assert dll.len == 0
        dll.push_front(1)
        assert dll.len == 1
        dll.push_front(2)
        assert dll.len == 2

        assert dll.pop_front() == 2
        assert dll.len == 1
        assert dll.pop_front() == 1
        assert dll.len == 0

    def test_ddl_back(self):
        dll = DoublyLinkedList[int]()
        assert dll.len == 0
        dll.push_back(1)
        assert dll.len == 1
        dll.push_back(2)
        assert dll.len == 2

        assert dll.pop_back() == 2
        assert dll.len == 1
        assert dll.pop_back() == 1
        assert dll.len == 0

    def test_dll_front_back(self):
        dll = DoublyLinkedList[int]()
        assert dll.len == 0
        dll.push_front(1)
        assert dll.len == 1
        dll.push_back(2)
        assert dll.len == 2
        dll.push_front(3)
        assert dll.len == 3

        assert dll.pop_front() == 3
        assert dll.len == 2
        assert dll.pop_back() == 2
        assert dll.len == 1
        assert dll.pop_front() == 1
        assert dll.len == 0


if __name__ == "__main__":
    unittest.main()
