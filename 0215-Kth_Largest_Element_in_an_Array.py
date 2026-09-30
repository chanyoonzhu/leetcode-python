"""
- https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
- sort -> max heap -> quickselect
"""

"""
- sort
- O(nlogn), O(1)
"""
class Solution: 
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """   
        nums.sort()
        return nums[-k]

"""
- max heap
- O(klogn), O(n)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        res = 0
        for _ in range(k):
            res = heapq.heappop(h)
        return -res

"""
- max heap
- O(nlogk), O(k)
"""
class Solution: 
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return heapq.nlargest(k, nums)[-1]

"""
- quick select - recursive
- time: O(n) like quick select, but only "sort" one partition each time, merge to O(n) on average, worst case is O(n^2) if reversely sorted
- space: O(1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)
        
    def quickSelect(self, nums, start, end, k):
        idx = self.partition(nums, start, end)
        if idx == k - 1:
            return nums[idx]
        elif idx < k - 1:
            return self.quickSelect(nums, idx + 1, end, k)
        else:
            return self.quickSelect(nums, start, idx - 1, k)
        
    def partition(self, nums, start, end):
        pivot = nums[end]
        idx = start
        for ptr in range(start, end):
            if nums[ptr] >= pivot:
                nums[idx], nums[ptr] = nums[ptr], nums[idx]
                idx += 1
        nums[idx], nums[end] = pivot, nums[idx]
        return idx

"""
- quick select - iterative
- time: O(n) like quick select, but only "sort" one partition each time, merge to O(n) on average, worst case is O(n^2) if reversely sorted
- space: O(1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            idx = self.partition(nums, l, r) # num[idx] is guaranteed to have the correct sorted position
            if idx == k - 1:
                return nums[idx]
            elif idx > k - 1:
                r = idx - 1
            else:
                l = idx + 1
        
    def partition(self, nums, start, end):
        pivot = nums[end]
        idx = start
        for i in range(start, end):
            if nums[i] >= pivot:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[end] = pivot, nums[idx]
        return idx
        
        
        