class Node(object):

    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_node(self.root,value)

    def insert_node(self,node,value):
        if node:
            if value < node.data:
                if node.leftchild:
                    self.insert_node(node.leftchild,value)
                else:
                    node.leftchild = Node(value)
            else:
                if node.rightchild:
                    self.insert_node(node.rightchild,value)
                else:
                    node.rightchild = Node(value)

    def in_order_traversal(self,node):
        '''LeftChild->Parent->RightChild'''
        if node:
            self.in_order_traversal(node.leftchild)
            print(node.data)
            self.in_order_traversal(node.rightchild)

    def search(self,value):
        return self.search_value(self.root,value)

    def search_value(self,node,value):
        if not node:
            return False
        if value < node.data:
            return self.search_value(node.leftchild,value)
        elif value > node.data:
            return self.search_value(node.rightchild,value)
        else:
            return True

    def delete(self,value):
        self.root = self.delete_node(self.root,value)

    def delete_node(self,node,value):
        if not node:
            return node
        if value < node.data:
            node.leftchild = self.delete_node(node.leftchild,value)
        elif value > node.data:
            node.rightchild = self.delete_node(node.rightchild,value)
        else:
            if not node.leftchild and not node.rightchild:
                del node
                return None
            elif not node.leftchild:
                temp_node = node.rightchild
                del node
                return temp_node
            elif not node.rightchild:
                temp_node = node.leftchild
                del node
                return temp_node
            else:
                temp_node = self.get_predecessor(node.leftchild)
                node.data = temp_node.data
                node.leftchild = self.delete_node(node.leftchild,temp_node.data)
        return node

    def get_predecessor(self,node):
        '''Left side highest value'''
        if node.rightchild:
            return self.get_predecessor(node.rightchild)
        return node

    def get_successor(self,node):
        '''Right side lowest value'''
        if node.leftchild:
            return self.get_successor(node.leftchild)
        return node
