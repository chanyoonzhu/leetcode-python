class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [0] * 300
        self.time = 0
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.updateHit(timestamp, 1)
        
            
    def updateHit(self, timestamp, isHit):
        prevIdx = self.time % 300 - 1
        diff = timestamp - self.time
        self.time = timestamp
        idx = self.time % 300 - 1
        
        if diff <= 300:
            if prevIdx > idx:
                for i in range(prevIdx+1, 300):
                    self.hits[i] = 0
                for i in range(0, idx+1):
                    self.hits[i] = 0
            else:
                for i in range(prevIdx+1, idx+1):
                    self.hits[i] = 0
            self.hits[idx] += isHit
        else:
            for i in range(300):
                self.hits[i] = 0
            self.hits[idx] += isHit
            
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.updateHit(timestamp, 0)
        return sum(self.hits)
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)