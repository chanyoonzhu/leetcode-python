"""
- hashmap + priority queue
- intuition: greedily uses letter with most count (count maintained in a heap), push back to heap in the next round to avoid using the same char again
- O(nlogn, O(n))
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        res, counter = [], Counter(s)
        h = [(-count, c) for c, count in counter.items()]
        heapq.heapify(h)
        prev_count, prev_c = 0, None # stores previously used char and count
        while h:
            neg_count, c = heapq.heappop(h)
            res.append(c)
            if prev_count < 0: # easy to miss: only push when count greater than 0 (neg count < 0)
                heapq.heappush(h, (prev_count, prev_c))
            prev_count, prev_c = neg_count + 1, c
        if len(res) != len(s): return ""
        return ''.join(res)