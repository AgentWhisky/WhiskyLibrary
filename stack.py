
# FILO Stack Class
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
