class LinkedListNode(object):
    """Linked list node class"""

    def __init__(self, data, next=None):
        """Initialize data when node is instantiated"""

        self.data = data

        # next is LinkedListNode
        self.next = next


class LinkedList(object):
    """Singly or doubly linked list class"""

    def __init__(self, head, tail):
        """Initialize data when node is instantiated"""

        # head and tail are LinkedListNodes
        self.head = head
        self.tail = tail


class DoublyLinkedListNode(object):
    """Doubly linked list node class"""

    def __init__(self, data, next=None, previous=None):
        """Initialize data when node is instantiated"""

        self.data = data

        # previous and next are DoublyLinkedListNode
        self.previous = previous
        self.next = next


class TreeNode(object):
    """Tree node class"""

    def __init__(self, data):
        """Initialize data when node is instantiated"""

        self.data = data

        # children is a list of TreeNodes
        self.children = []


class Tree(object):
    """Tree class"""

    def __init__(self, root):
        """Initialize data when node is instantiated"""

        # root is a TreeNode
        self.root = root

        # is this even necessary? Why not just refer to the 
        # root node directly? 

        # A tree class is good to store data that relates to
        # the tree as a whole, and not an individual node. 
        # Not always necessary. 


class GraphNode(object):
    """Graph node class"""

    def __init__(self, data):
        """Initialize data when node is instantiated"""

        self.data = data

        # adjacency_list list of GraphNode
        self.adjacency_list = set()


class Graph(object):
    """Graph class"""

    def __init__(self):
        """Initialize data when node is instantiated"""

        self.nodes = set()