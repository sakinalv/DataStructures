class Queue(object):

    def __init__(self):
        self.queue = list()

    def enqueue(self,value):
        self.queue.insert(0,value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def is_empty(self):
        return not len(self.queue)

    def print_queue(self):
        print(self.queue)
