class Node(object):

    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 0

class AVL(object):

    def __init__(self):
        self.root = None

    def calc_height(self,node):
        if not node:
            return -1
        return node.height

    def calc_balance(self,node):
        if not node:
            return 0
        return self.calc_height(node.leftchild) - self.calc_height(node.rightchild)

    def insert(self,value):
        self.root = self.insert_node(self.root,value)

    def insert_node(self,node,value):
        if not node:
            return Node(value)
        if value < node.data:
            node.leftchild = self.insert_node(node.leftchild,value)
        else:
            node.rightchild = self.insert_node(node.rightchild,value)

        node.height = max(self.calc_height(node.leftchild),self.calc_height(node.rightchild)) + 1
        return self.settle_voilations(node)

    def settle_voilations(self,node):
        balance = self.calc_balance(node)
        if balance > 1 and self.calc_balance(node.leftchild) >= 0:
            return self.rotate_right(node)
        elif balance > 1 and self.calc_balance(node.leftchild) < 0:
            node.leftchild = self.rotate_left(node.leftchild)
            return self.rotate_right(node)
        elif balance < -1 and self.calc_balance(node.rightchild) <= 0:
            return self.rotate_left(node)
        elif balance < -1 and self.calc_balance(node.rightchild) > 0:
            node.rightchild = self.rotate_right(node.rightchild)
            return self.rotate_left(node)
        return node

    def rotate_right(self,node):
        temp_left = node.leftchild
        t = temp_left.rightchild
        temp_left.rightchild = node
        node.leftchild = t

        node.height = max(self.calc_height(node.leftchild),self.calc_height(node.rightchild)) + 1
        temp_left.height = max(self.calc_height(temp_left.leftchild),self.calc_height(temp_left.rightchild)) + 1

        return temp_left

    def rotate_left(self,node):
        temp_right = node.rightchild
        t = temp_right.leftchild
        temp_right.leftchild = node
        node.rightchild = t

        node.height = max(self.calc_height(node.leftchild),self.calc_height(node.rightchild)) + 1
        temp_right.height = max(self.calc_height(temp_right.leftchild),self.calc_height(temp_right.rightchild)) + 1

        return temp_right

    def in_order_traversal(self,node):
        if node:
            self.in_order_traversal(node.leftchild)
            print(node.data)
            self.in_order_traversal(node.rightchild)

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
                temp_right = node.rightchild
                del node
                return temp_right
            elif not node.rightchild:
                temp_left = node.leftchild
                del node
                return temp_left
            else:
                temp_node = self.get_predecessor(node.leftchild)
                node.data = temp_node.data
                node.leftchild = self.delete_node(node.leftchild,temp_node.data)
        node.height = max(self.calc_height(node.leftchild),self.calc_height(node.rightchild)) + 1
        return self.settle_voilations(node)

    def get_predecessor(self,node):
        if node.rightchild:
            return self.get_predecessor(node.rightchild)
        return node

    def get_successor(self,node):
        if node.leftchild:
            return self.get_successor(node.leftchild)
        return node
