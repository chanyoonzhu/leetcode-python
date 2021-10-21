from collections import deque

"""
- brutal force sliding window: time exceeded
- O(Nk), O(N−k+1)
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max([nums[j] for j in range(i, i + k)]))
        return res

"""
- priority queue
- O(n * log(k)), O(k)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i >= k - 1:
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
        return result

"""
- sliding window with monotonic queue
- O(n), O(k)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()
        result = []
        
        for i in range(len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if i < k - 1: continue
            while q and q[0] <= i - k:
                q.popleft()
            result.append(nums[q[0]])
        return result

s = Solution()
# s.maxSlidingWindow_optimized([1,3,-1,-3,5,3,6,7], 3)
s.maxSlidingWindow_optimized([7,6,5,4,3,5,6], 3)