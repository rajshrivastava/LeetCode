from collections import deque
from threading import Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en, self.de = Lock(), Lock()
        self.q = deque([])
        self.capacity = capacity
        self.de.acquire()
        
    def enqueue(self, element: int) -> None:
        self.en.acquire()
        self.q.append(element)
        if len(self.q) < self.capacity:
            self.en.release()
        if self.de.locked():
            self.de.release()
        

    def dequeue(self) -> int:
        self.de.acquire()
        val = self.q.popleft()
        if len(self.q):
            self.de.release()
        if self.en.locked():
            self.en.release()
        return val

    def size(self) -> int:
        return len(self.q)
        
