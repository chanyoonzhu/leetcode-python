"""
- similar: 358
"""
"""
- greedy
- intuition: greedily fill the odd index, then even index, using chars with most common freq to least
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        res, counter = [''] * N, Counter(s)
        sorted_s = ''.join([c * count for c, count in counter.most_common()])
        s_i = 0
        for i in range(0, N, 2): # fill odd index
            res[i] = sorted_s[s_i]
            s_i += 1
        for i in range(1, N, 2): # fill even index
            res[i] = sorted_s[s_i]
            if res[i] == res[i-1]: return "" # consecutive chars can't be the same
            s_i += 1
        return "".join(res)

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