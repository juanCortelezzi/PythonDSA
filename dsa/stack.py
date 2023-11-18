class Stack:
    """
    please just use an array ...

    If you happen to have a case in which an actual stack in the heap is
    better than an array, what are you doing here? you are clearly more
    knowledgeable than I am.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def lemma():
        pass
