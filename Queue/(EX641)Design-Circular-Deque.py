from collections import deque

class MyCircularDeque(object):

    def __init__(self, k):
        self.queue = deque()
        self.maxSize = k

    def insertFront(self, value):
        if self.isFull():
            return False
        self.queue.appendleft(value)
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.queue.append(value)
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.queue.popleft()
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.queue.pop()
        return True

    def getFront(self):
        return self.queue[0] if not self.isEmpty() else -1

    def getRear(self):
        return self.queue[-1] if not self.isEmpty() else -1

    def isEmpty(self):
        return not self.queue

    def isFull(self):
        return len(self.queue) == self.maxSizeit 