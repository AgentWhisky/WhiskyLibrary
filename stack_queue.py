from collections import deque


# FILO Stack Class*
class Stack:
    def __init__(self):
        self._stack = []

    # Push item onto Stack
    def push(self, item):
        self._stack.append(item)

    # Pop Item from stack
    def pop(self):
        return self._stack.pop()

    # Return is stack empty
    def isEmpty(self):
        return len(self._stack) == 0

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return 'Stack(' + str(self._stack) + ')'


# FIFO Queue Class
# Can be declared with maxlen
class Queue(deque):

    # Add item to queue
    def enqueue(self, item):
        self.append(item)

    # Remove Item from queue
    def dequeue(self):
        return self.popleft()

    # Return is queue empty
    def isEmpty(self):
        return len(self) == 0
