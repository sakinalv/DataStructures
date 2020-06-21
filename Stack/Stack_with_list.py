class Stack(object):

    def __init__(self):
        self.stack = list()

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return not len(self.stack)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def print_stack(self):
        print(self.stack)
