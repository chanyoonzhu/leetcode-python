"""
- sliding window + priority queue (*2)
- O(nlogn), O(n)
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxh, minh = [], []
        res = l = 0
        for r, a in enumerate(nums):
            heapq.heappush(maxh, (-a, r))
            heapq.heappush(minh, (a, r))
            while -maxh[0][0] - minh[0][0] > limit:
                l = min(maxh[0][1], minh[0][1]) + 1
                while maxh[0][1] < l: heapq.heappop(maxh)
                while minh[0][1] < l: heapq.heappop(minh)
            res = max(res, r - l + 1)
        return res

"""
- sliding window + monotonic queue (*2)
- O(n), O(n)
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
    
        maxq = collections.deque()
        minq = collections.deque()
        result = l = 0
        for r, n in enumerate(nums):
            while minq and n <= nums[minq[-1]]:
                minq.pop()
            minq.append(r)
            while maxq and n >= nums[maxq[-1]]:
                maxq.pop()
            maxq.append(r)
            while nums[maxq[0]] - nums[minq[0]] > limit:
                l += 1
                if minq[0] < l: minq.popleft()
                if maxq[0] < l: maxq.popleft()
            result = max(result, r - l + 1)
        return result