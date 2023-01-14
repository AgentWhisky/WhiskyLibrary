import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []

    # Enqueue item by priority
    def enqueue(self, item, priority):
        heapq.heappush(self._queue, (priority, item))

    # Pop Item from queue and return
    def dequeue(self):
        return heapq.heappop(self._queue)[1]

