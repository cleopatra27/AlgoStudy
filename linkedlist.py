'''
One of the problems this solves is insert and delete time instead of using a list with higher time complexity.
Nodes are the building blocks for lists
'''

class Node:

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    head = None

    def __init__(self):
        self.head = None


N1 = Node(10)
N1.next_node = Node(20)
print(N1.next_node)
