#!/usr/bin/python3
"""Singly Linked List module"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Initialize a node of a singly linked list

        Args:
            data (int): Data.
            next_node (:obj:`Node`, optional): Next linkedlist node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the head of the singly linked list"""
        self.head = None

    def __str__(self):
        """String representation of singly linked list"""
        result = ""
        current = self.head
        while current:
            result += "{:d}".format(current.data)
            if current.next_node:
                result += "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.head is None:
            new_node.next_node = self.head
            self.head = new_node
        elif self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
