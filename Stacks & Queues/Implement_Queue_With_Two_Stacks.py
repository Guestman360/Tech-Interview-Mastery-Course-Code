  class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack2) == 0:

            # Move items from in_stack to out_stack, reversing order
            while len(self.stack1) > 0:
                newItem = self.stack1.pop()
                self.stack2.append(newItem)

            # If out_stack is still empty, raise an error
            if len(self.stack2) == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.stack2.pop()