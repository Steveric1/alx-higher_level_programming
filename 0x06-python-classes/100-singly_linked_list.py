#!/usr/bin/python3
"""Node and Singlylinkedlist class"""


class Node:
    """A class Node"""

    def __init__(self, data, next_node=None):
        """Initialize the Node class with two fields
        Args:
            data(int): the node data
            next_node(Node): next node to help in traversing the linkedlist
            """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or retrieve a value"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set a value"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a singlylinkedlist"""

    def __init__(self, head=None):
        """Initialize the singlylinkedlist with head fields
        Args:
            head: the head of the singlylinkedlist
            """
        self.__head = head

    def __str__(self):
        """Return the string representation of the singlylinkedlist"""
        current = self.__head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return ('\n'.join(result))

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position."""
        new_node = Node(value)

        """Check if the head is empty and if value is smaller than the
        head, insert at the beginning"""

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            """Traverse the list to find the correct position"""
            while (current.next_node is not None
                    and current.next_node.data < value):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
