#!/usr/bin/python3
# File: 100-singly_linked_list.py
# Author: Oluwatobiloba Light
"""Defines a singly linked list."""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.

    Methods:
        data(): Retrieve the data stored in the node.
        data(value): Set the data stored in the node.
        next_node(): Retrieve the next node in the linked list.
        next_node(value): Set the next node in the linked list.

    Raises:
        TypeError: If the provided data is not an integer.
        TypeError: If the provided next_node is not None or a Node object.

    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with the given data and optional next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list
                              (default is None).
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the provided data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If the provided next_node is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        __head: The head node of the linked list.

    Methods:
        __init__(): Initializes an empty linked list.
        sorted_insert(value): Inserts a new Node into the list at the
        correct sorted position.
        __str__(): Returns a string representation of the linked list.

    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the list at the correct sorted position.

        Args:
            value: The value to be inserted into the linked list.

        """
        new_node = Node(value)
        if self.__head == None:
            new_node.next_node = None
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        current = self.__head
        result = []
        while current.next_node is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
