#!/usr/bin/python3
# Author: Adamu Muhammad
"""singly linked list module"""


class Node:
    """define node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter attrib for data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """set data attrib"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node value
        Returns: next_node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets next_node"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """define singly linked list"""

    def __init__(self):
        """initialize list"""
        self.head = None

    def __str__(self):
        """make list print self"""
        pr = ""
        pos = self.head
        while pos:
            pr += str(pos.data) + "\n"
            pos = pos.next_node
        return (pr[:-1])

    def sorted_insert(self, value):
        """insert sequencially
        Args: value - of node
        """
        val = Node(value)
        if not self.head:
            self.head = val
            return
        if value < self.head.data:
            val.next_node = self.head
            self.head = val
            return
        pos = self.head
        while pos.next_node and pos.next_node.data < value:
            pos = pos.next_node
        if pos.next_node:
            val.next_node = pos.next_node
        pos.next_node = val
