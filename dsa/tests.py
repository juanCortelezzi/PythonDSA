import unittest
from doubly_linked_list import DoublyLinkedList
from binary_tree import BinarySearchTree
from linked_list import LinkedList
from binary_search import binary_search


class TestBinarySearchTree(unittest.TestCase):
    def test_binary_search_tree_insertion(self):
        bst = BinarySearchTree[int]()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        assert bst.root != None and bst.root.value == 2
        assert bst.root.left != None and bst.root.left.value == 1
        assert bst.root.right != None and bst.root.right.value == 3
        assert bst.size == 3

    def test_binary_search_tree_search(self):
        bst = BinarySearchTree[int]()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        assert bst.has(2) == True
        assert bst.has(1) == True
        assert bst.has(3) == True
        assert bst.has(4) == False

    def test_binary_search_tree_deletion(self):
        bst = BinarySearchTree[int]()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.delete(2)
        assert bst.root != None and bst.root.value == 3
        assert bst.root.left != None and bst.root.left.value == 1
        assert bst.size == 2

    def test_binary_search_tree_complex_deletion(self):
        bst = BinarySearchTree[int]()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        bst.delete(2)
        assert bst.root != None and bst.root.value == 3
        assert bst.root.left != None and bst.root.left.value == 1
        assert bst.root.right != None and bst.root.right.value == 4
        assert bst.root.right.right != None and bst.root.right.right.value == 5
        assert bst.size == 4

    def test_binary_search_tree_preorder(self):
        bst = BinarySearchTree[int]()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        assert bst.preorder_traversal() == "2 -> 1 -> 3 -> NULL"

    def test_binary_search_tree_inorder(self):
        bst = BinarySearchTree[int]()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        assert bst.inorder_traversal() == "1 -> 2 -> 3 -> NULL"


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        assert binary_search(arr, 6) == 5
        assert binary_search(arr, 8) == 7
        assert binary_search(arr, 1) == 0
        assert binary_search(arr, 4) == 3
        assert binary_search(arr, 10) == None


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
