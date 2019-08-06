class MinStack(object):

    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, item):
        """Add a new item onto the top of our stack."""
        self.stack.push(item)

        # If the item is greater than or equal to the last item in maxes_stack,
        # it's the new max! So we'll add it to maxes_stack.
        if self.min_stack.peek() is None or item <= self.min_stack.peek():
            self.min_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.min_stack.peek():
            self.min_stack.pop()

        return item

    def getMin(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.min_stack.peek()