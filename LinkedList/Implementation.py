class Node(object):

    def __init__(self,data):
        self.data = data
        self.nextnode = None

class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            curr_head = self.head
            while curr_head.nextnode:
                curr_head = curr_head.nextnode
            curr_head.nextnode = Node(value)

    def print_list(self):
        curr_head = self.head
        while curr_head:
            print(curr_head.data)
            curr_head = curr_head.nextnode

    def search(self,value):
        curr_head = self.head
        while curr_head:
            if curr_head.data == value:
                return True
            curr_head = curr_head.nextnode
        return False

    def insert_at_head(self,value):
        new_node = Node(value)
        new_node.nextnode = self.head
        self.head = new_node

    def delete(self,value):
        if self.head and self.head.data == value:
            self.head = self.head.nextnode
        else:
            curr_head = self.head
            prev = None
            while curr_head and curr_head.data != value:
                prev = curr_head
                curr_head = curr_head.nextnode
            if curr_head:
                prev.nextnode = curr_head.nextnode
                curr_head.nextnode = None
