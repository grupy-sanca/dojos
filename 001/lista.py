"""Dojo Grupy Sanca - 27/07/2016
"""


class Node:
    """
    >>> Node(1)
    Node(1)
    >>> no = Node('abc')
    >>> no
    Node('abc')
    """
    next = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Node({!r})'.format(self.value)


class List:
    """
    >>> lista = List()
    >>> lista
    List()
    >>> no = Node(1)
    >>> no.next
    >>> lista.head
    """
    head = None

    def __repr__(self):
        return 'List()'

    def insert(self, value):
        """
        >>> lista = List()
        >>> lista.insert('ab')
        >>> lista.print()
        ab
        >>> lista.insert('cd')
        >>> lista.print()
        ab
        cd
        >>> lista.insert('ef')
        >>> lista.print()
        ab
        cd
        ef
        """
        new_node = Node(value)

        node = self.head
        if node is None:
            self.head = new_node
            return

        while node.next is not None:
            node = node.next
        node.next = new_node

    def print(self):
        """
        >>> lista = List()
        >>> lista.insert(2)
        >>> lista.print()
        2
        """
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def pop(self):
        """
        >>> lista = List()
        >>> lista.insert('ab')
        >>> lista.insert('cd')
        >>> lista.insert('ef')
        >>> lista.pop()
        Node('ef')
        >>> lista.print()
        ab
        cd
        >>> lista.pop()
        Node('cd')
        >>> lista.print()
        ab
        """
        last = self.head
        penult = None
        while last is not None:
            if last.next is None:
                break
            penult = last
            last = last.next
        if penult:
            penult.next = None
        else:
            self.head = None
        return last

    def remove(self, value):
        """
        >>> lista = List()
        >>> lista.insert('ab')
        >>> lista.insert('cd')
        >>> lista.remove('ab')
        >>> lista.print()
        cd
        >>> lista = List()
        >>> lista.insert(1)
        >>> lista.insert(2)
        >>> lista.insert(3)
        >>> lista.insert(4)
        >>> lista.remove(1)
        >>> lista.print()
        2
        3
        4
        >>> lista.remove(3)
        >>> lista.print()
        2
        4
        >>> lista.remove(4)
        >>> lista.print()
        2
        >>> lista.remove(2)
        >>> lista.print()
        """
        node = self.head
        penult = None
        while node is not None:
            if node.value == value:
                if node == self.head:
                    self.head = node.next
                elif node.next is None:
                    penult.next = None
                else:
                    penult.next = node.next
                break
            penult = node
            node = node.next
