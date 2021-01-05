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
    - quick select # todo
    """