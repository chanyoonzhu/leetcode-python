from threading import Barrier, Semaphore

"""
- Concurrency
- O(n), O(1)
"""
class H2O:
    def __init__(self):
        self.b = Barrier(3) # if a thread reaches it, it can cross it, only if a predefined number (3 in our case) of other threads have also arrived.
        self.h = Semaphore(2) # a Semaphore -- trying to acquire it, is possible if there are tokens left. Otherwise the thread that tried is asked to wait until a different thread returns the tokens it was using
        self.o = Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        self.h.acquire()
        self.b.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h.release()
        """ or
        with self.sem_h:
            self.bar_assembling.wait()
            releaseHydrogen()
        """


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        self.o.acquire()
        self.b.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o.release()
        """or
        with self.sem_o:
            self.bar_assembling.wait()
            releaseOxygen()
        """