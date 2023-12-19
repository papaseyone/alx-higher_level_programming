#!/usr/bin/python3
"""
Defines the classes Node and SinglyLinkedList
"""


class Node:
    """
    Class that defines properties of a Node.

    Attributes:
        __data (int): Data field of a node.
    """
    def __init__(self, data, next_node=None):
        """
        Creates new instances of a node.

        Args:
            data (int): Data field of a node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data field of an instance.

        Returns:
            int: Data field of a node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Property setter for data.

        Args:
            value (int): Data field of a node.

        Raises:
            TypeError: Data must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next_node instance.

        Returns:
            Node: The next_node instance.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Property setter for next_node.

        Args:
            value (Node): Next node of a Node.

        Raises:
            TypeError: next_node must be a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines properties of SinglyLinkedList.

    Attributes:
        __head (Node): Head of the SinglyLinkedList.
    """
    def __init__(self):
        """
        Creates new instances of SinglyLinkedList.

        Args:
            __head (Node): Head of the SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        Represents the class objects as a string.

        Returns:
            str: The class object represented as a string.
        """
        temp_var = self.__head
        print_node = []
        while temp_var:
            print_node.sort()
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        print_node.sort(key=int)
        return "\n".join(print_node)

    def sorted_insert(self, value):
        """
        Inserts a new node at a given position.

        Args:
            value: Value.
        """
        if self.__head is None:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
