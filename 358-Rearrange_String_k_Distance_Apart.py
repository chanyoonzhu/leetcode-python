"""
- hashmap + priority queue
- intuition: greedily uses letter with most count (count maintained in a heap), mainting a cooling mem to store number that cannot be used next round
- O(nlogn, O(n))
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1: 
            return s
        counter = Counter(s)
        freqs = [(-counter[k], k) for k in counter]
        heapq.heapify(freqs)        
        cooling = {}
        res = []
        while freqs:
            freq, c = heapq.heappop(freqs)
            res.append(c)
            freq += 1
            if freq < 0:                
                cooling[c] = freq
            if len(res) >= k and res[-k] in cooling:
                coolingFreq, coolingC = cooling[res[-k]], res[-k]
                del cooling[res[-k]]
                heapq.heappush(freqs,(coolingFreq, coolingC))        
        return ''.join(res) if len(res) == len(s) else ""