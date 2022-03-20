from threading import Semaphore

"""
- Concurrency
- O(n), O(n)
"""
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.pushing = Semaphore(capacity)
        self.pulling = Semaphore(0) # cannot dequeue when empty           
        self.queue = collections.deque() # append and popleft is threadsafe, otherwise need a lock
        

    def enqueue(self, element: int) -> None:
        self.pushing.acquire() # subtract 1 from self.pushing semaphore     
        self.queue.append(element)              
        self.pulling.release() # add 1 to self.pulling semaphore 
        

    def dequeue(self) -> int:
        self.pulling.acquire()                
        res = self.queue.popleft()                
        self.pushing.release()
        return res


    def size(self) -> int:
        return len(self.queue)


"""
- not assume queue is thread-safe
"""
import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
      
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
      self.pushing.acquire()
      self.editing.acquire()
      
      self.queue.append(element)
      
      self.editing.release()
      self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        self.pushing.release()
        return res

    def size(self) -> int:
      return len(self.queue)