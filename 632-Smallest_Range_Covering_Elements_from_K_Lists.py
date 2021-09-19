"""
- priority queue
- O(nlogm), O(m)
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)
        q = [(numlist[0], i, 0) for i, numlist in enumerate(nums)] # q stores: num, i, j
        
        right = max([n for n, _, _ in q])
        left_right = float("-inf"), float("inf")
        heapq.heapify(q)
        while q:
            left, i, j = heapq.heappop(q)
            if right - left < left_right[1] - left_right[0]:
                left_right = left, right
            if j == len(nums[i]) - 1: return left_right
            right = max(right, nums[i][j + 1])
            heapq.heappush(q, (nums[i][j + 1], i, j + 1))