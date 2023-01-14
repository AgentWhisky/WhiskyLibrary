from collections import deque


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
