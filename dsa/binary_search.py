from typing import Optional
from typing import TypeVar, Optional

T = TypeVar("T", bound=int | float)


def binary_search(arr: list[T], item: T) -> Optional[int]:
    """This should support any comparable type but python generics are trash."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid

        if item > arr[mid]:
            low = mid + 1
            continue

        if item < arr[mid]:
            high = mid - 1
            continue


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert binary_search(arr, 6) == 5
    assert binary_search(arr, 8) == 7
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 4) == 3
    assert binary_search(arr, 10) == None


if __name__ == "__main__":
    main()
