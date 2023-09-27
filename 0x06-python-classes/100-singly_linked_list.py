#!/usr/bin/python3
"""Creating a linked list with python classes"""


class Node:
    """Defining a node of a singly linked list"""
    def __init__(self, data, next_node=None):

        """intialize a new node

        Args:
            data(int): the value of the node
            next_node(Node): the next node in the list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter to retrive the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """A setter to set the data to a given value"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """A getter to get the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Represnts a single linked list"""
    def __init__(self):
        """Defining class attributes"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting a new node in a linked list with
            increasing order"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
            new.next_node = None
        elif (self.__head.data > value):
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """special method to print the class"""
        data_lst = []
        tmp = self.__head
        while tmp is not None:
            data_lst.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(data_lst))
