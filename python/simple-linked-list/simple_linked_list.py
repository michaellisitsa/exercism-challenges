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
        try:
            current_node = self.head()
            yield current_node.value()
            while current_node and current_node.next():
                nextNode = current_node.next()
                yield nextNode.value()
                current_node = nextNode
        except (EmptyListException, AttributeError):
            pass

    def __len__(self):
        """
        We're calling len() in the tests to determine length of list
        """
        length = 0
        try:
            current_node: Node = self.head()
            length += 1
        except EmptyListException:
            # Do not throw an exception on accessing head.
            # We want to still have this query accessible
            # as the LinkedList may be empty to start but filled with push
            return length

        while current_node and current_node.next():
            # Checking current_node
            length += 1
            current_node = current_node.next()
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
            current_value = current_head.value()
            new_head = current_head.next()
            if new_head:
                self._head = new_head
            else:
                # type error as we're resetting the head, and the current type doesn't allow this
                # Horrible hack because we don't want to set it to None, otherwise it won't error in the try blocks
                del self._head
        except AttributeError:
            return None
        return current_value

    def reversed(self):
        return LinkedList(list(self))
