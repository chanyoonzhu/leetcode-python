class Solution(object):

    """
    - sort
    - O(nlogn), O(1)
    """
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
    - O(nlogk), O(k)
    """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return heapq.nlargest(k, nums)[-1]

    """
    - quick select - my solution
    - time: O(n) like quick select, but only "sort" one partition each time, merge to O(n) on average, worst case is O(n^2) if reversely sorted
    - space: O(1)
    """
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums, 0, len(nums) - 1, k)
        
    def quickSort(self, nums, start, end, k):
        idx = self.partition(nums, start, end)
        if idx + 1 == k:
            return nums[idx]
        elif idx + 1 < k:
            return self.quickSort(nums, idx + 1, end, k)
        else:
            return self.quickSort(nums, start, idx - 1, k)
    
    def partition(self, nums, start, end):
        pivot = nums[end]
        idx = start
        for i in range(start, end):
            if nums[i] >= pivot:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
        nums[idx], nums[end] = pivot, nums[idx]
        return idx