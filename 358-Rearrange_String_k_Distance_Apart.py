"""
- hashmap + priority queue
- intuition: greedily uses letter with most count (count maintained in a heap), mainting a cooling mem to store number that cannot be used next round
- O(nlogn, O(n))
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1: return s;
        res = []
        
        h = [(-count, c) for c, count in Counter(s).items()]
        heapq.heapify(h)
        
        while h:
            if len(h) < k and h[0][0] != -1: return "" # can only have 1 element left when len(h) < k
            
            cooling = [None] * min(k, len(h)) # easy to miss: h have less than k elements
            for i in range(len(cooling)):
                res.append(h[0][1])
                cooling[i] = (heapq.heappop(h))
                
            for count, c in cooling:
                if count < -1:
                    heapq.heappush(h, (count + 1, c))
        return "".join(res)
    
"""
- greedy
- O(n) + O(26log26) = O(n), O(n)
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        N = len(s)
        if k < 2: return s
        
        counter = Counter(s)
        counter = collections.Counter(s)
        counts = [(count, c) for c, count in counter.items()]
        counts.sort(key=lambda x: -x[0]) # O(26log26)
        
        max_count = counts[0][0]
        buckets = [[] for _ in range(max_count)]
        
        i = 0
        for count, c in counts:
            if count == max_count: # char has the same count as max_count, so must spread it evently in all buckets.
                for bucket in buckets:
                    bucket.append(c)
            else: # char has counts smaller than max_count, don't use the last bucket to maximize the chars between each two adjacent buckets.
                while count > 0:
                    buckets[i].append(c)
                    i = (i + 1) % (max_count - 1)
                    count -= 1
        res = []
        for i, bucket in enumerate(buckets):
            if i != max_count - 1 and len(bucket) < k: return '' # only last bucket have have fewer than k elements
            res += bucket
        return ''.join(res)