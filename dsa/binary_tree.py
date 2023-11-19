from typing import Generic, Optional, TypeVar

T = TypeVar("T", bound=int | float)


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.left: Optional["Node[T]"] = None
        self.right: Optional["Node[T]"] = None


class BinarySearchTree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None
        self.size = 0

    def __rec_insert(self, node: Optional[Node[T]], new_node: Node[T]):
        if node == None:
            return new_node

        if new_node.value > node.value:
            node.right = self.__rec_insert(node.right, new_node)
        elif new_node.value <= node.value:
            node.left = self.__rec_insert(node.left, new_node)

        return node

    def insert(self, value: T):
        self.size += 1
        self.root = self.__rec_insert(self.root, Node(value))

    def __rec_inorder_traversal(self, s: str, node: Optional[Node[T]]) -> str:
        if node == None:
            return s

        s = self.__rec_inorder_traversal(s, node.left)
        s += f"{node.value} -> "
        s = self.__rec_inorder_traversal(s, node.right)
        return s

    def inorder_traversal(self) -> str:
        return self.__rec_inorder_traversal("", self.root) + "NULL"

    def __rec_preorder_traversal(self, s: str, node: Optional[Node[T]]) -> str:
        if node == None:
            return s

        s += f"{node.value} -> "
        s = self.__rec_preorder_traversal(s, node.left)
        s = self.__rec_preorder_traversal(s, node.right)
        return s

    def preorder_traversal(self) -> str:
        return self.__rec_preorder_traversal("", self.root) + "NULL"

    def __rec_has(self, node: Optional[Node[T]], value: T) -> bool:
        if node == None:
            return False

        if value > node.value:
            return self.__rec_has(node.right, value)

        if value < node.value:
            return self.__rec_has(node.left, value)

        return True

    def has(self, value: T) -> bool:
        return self.__rec_has(self.root, value)

    def __rec_min_node(self, node: Node[T]) -> T:
        if node.left:
            return self.__rec_min_node(node.left)

        return node.value

    def min_value(self) -> Optional[T]:
        if self.root == None:
            return

        return self.__rec_min_node(self.root)

    def __rec_delete(self, node: Optional[Node[T]], value: T):
        if node == None:
            return

        if value > node.value:
            node.right = self.__rec_delete(node.right, value)
            return node

        if value < node.value:
            node.left = self.__rec_delete(node.left, value)
            return node

        if node.left == None:
            return node.right

        if node.right == None:
            return node.left

        node.value = self.__rec_min_node(node.right)
        node.right = self.__rec_delete(node.right, node.value)
        return node

    def delete(self, value: T):
        self.size -= 1
        self.root = self.__rec_delete(self.root, value)


def main():
    t = BinarySearchTree[int]()
    t.insert(5)
    t.insert(2)
    t.insert(7)
    t.insert(1)
    t.insert(3)
    t.insert(6)
    t.insert(20)
    t.insert(15)
    t.insert(17)
    t.insert(30)
    print(t.preorder_traversal())
    t.delete(7)
    assert t.size == 9
    print(t.preorder_traversal())
    t.delete(5)
    assert t.size == 8
    print(t.preorder_traversal())


if __name__ == "__main__":
    main()
