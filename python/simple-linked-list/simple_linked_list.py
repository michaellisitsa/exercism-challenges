from __future__ import annotations


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message


class Node:
    _next: Node | None
    _value: int

    def __init__(self, value: int):
        """
        Each song is a number

        """
        # Store the value
        self._value = value

    def value(self) -> int:
        return self._value

    def next(self) -> Node | None:
        try:
            return self._next
        except:
            return None


class LinkedList:
    _head: Node | None

    def __init__(self, values=None):
        if values is None:
            return
        for value in values:
            self.push(value)

    def __iter__(self):
        """
        Supports looping through the list
        """
        pass

    def __len__(self):
        """
        We're calling len() in the tests to determine length of list
        """
        length = 0
        try:
            currentNode: Node | None = self.head()
            length += 1
        except EmptyListException:
            # Do not throw an exception on accessing head.
            # We want to still have this query accessible
            # as the LinkedList may be empty to start but filled with push
            return length

        while currentNode and currentNode.next():
            # Checking currentNode
            length += 1
            currentNode = currentNode.next()
        return length

    def head(self) -> Node:
        try:
            return self._head
        except:
            raise EmptyListException("The list is empty.")

    def push(self, value):
        """
        Push to the head of the linked list
        If head doesn't exist we don't need to except
        """
        newHead = Node(value)
        try:
            newHead._next = self.head()
        except EmptyListException:
            pass
        self._head = newHead

    def pop(self):
        try:
            # This all seems very ugly
            # Find a better way in python
            current_head = self.head()
            new_head = current_head.next()
            if new_head:
                self._head = new_head
            else:
                # type error as we're resetting the head, and the current type doesn't allow this
                self._head = None
        except AttributeError:
            return None
        return current_head.value()

    def reversed(self):
        pass


# Given a range of numbers
list = LinkedList([1, 2, 3, 4, 5])
len(list)
# Expect a linked list for each number
#
