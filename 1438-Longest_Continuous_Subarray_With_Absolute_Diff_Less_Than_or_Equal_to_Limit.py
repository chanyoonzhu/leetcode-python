"""
- sliding window + priority queue (*2)
- intuition: Absolute difference between min and max elements of subarray is smaller than limit. 
- O(nlogn), O(n)
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxh, minh = [], []
        res = l = 0
        for r, a in enumerate(nums):
            heapq.heappush(maxh, (-a, r))
            heapq.heappush(minh, (a, r))
            while -maxh[0][0] - minh[0][0] > limit: # nums[l:r+1] has diff greater than limit, need to move l to right
                l = min(maxh[0][1], minh[0][1]) + 1
                # lazy pop
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
    
        maxq = collections.deque() # mono-decreasing within l:r+1, maxq[0] - max
        minq = collections.deque() # mono-increasing within l:r+1, minq[0] - min
        result = l = 0
        for r, n in enumerate(nums):
            while minq and n <= nums[minq[-1]]:
                minq.pop()
            minq.append(r)
            while maxq and n >= nums[maxq[-1]]:
                maxq.pop()
            maxq.append(r)
            while nums[maxq[0]] - nums[minq[0]] > limit:
                l = min(maxq[0], minq[0]) + 1 # faster than l += 1
                if minq[0] < l: minq.popleft()
                if maxq[0] < l: maxq.popleft()
            result = max(result, r - l + 1)
        return result