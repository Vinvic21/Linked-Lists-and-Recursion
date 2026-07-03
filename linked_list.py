
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None  #initialized the head and set it to none


    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def recursive_sum(self, node=None):
        if node is None:
            node = self.head
        if node is None:
            return 0
        if node.next is None:
            return node.data
        return node.data + self.recursive_sum(node.next)
        
    def recursive_reverse(self):
        def _reverse(current, prev):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse(next_node, current)
        self.head = _reverse(self.head, None)

       
  
    def recursive_search(self, target):
        def _search(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return _search(node.next)
        return _search(self.head)


    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print(None)
      