"""
- array one-pass
- intuition: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/754682/Wall-of-bricks
- O(n), O(1)
"""
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = 0
        for x in target:
            if x > prev:
                res += x - prev
            prev = x
        return res

"""
- priority heap (my solution)
- TLE
"""
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        indexes = {}
        h = list(set(map(lambda x: -x, target)))
        heapq.heapify(h)
        result = 0
        for i, x in enumerate(target):
            if x not in indexes:
                indexes[x] = [i]
            else:
                heapq.heappush(indexes[x], i)
        while h:
            cur = -heapq.heappop(h)
            prev_i = heapq.heappop(indexes[cur])
            if h: heapq.heappush(indexes[-h[0]], prev_i)
            ops_diff = cur + h[0] if h else cur
            ops = ops_diff
            while indexes[cur]:
                cur_i = heapq.heappop(indexes[cur])
                if h: heapq.heappush(indexes[-h[0]], cur_i)
                if prev_i + 1 != cur_i:
                    ops += ops_diff
                prev_i = cur_i
            result += ops
        return result