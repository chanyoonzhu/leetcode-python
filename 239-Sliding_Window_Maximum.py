from collections import deque

class Solution(object):

    """
    - brutal force sliding window: time exceeded
    - O(Nk), O(N−k+1)
    """
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
    - sliding window: deque
    - O(N), O(N−k+1)

    Algorithm:
    Iterate over the array. At each step :
    Clean the deque :
    Keep only the indexes of elements from the current sliding window.
    Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.
    Append the current element to the deque.
    Append deque[0]， which is the maximum in the window, to the output.
    Return the output array.
    """
    class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        def clean_deque(i):
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            if deq and deq[0] == i - k:
                deq.popleft()
            # "sorts" deq 
            # if current item is larger than previous candidates, remove all previous candidates that are smaller than current
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
                
        deq = deque() # keep the index of candidates, with nums[index] ordered from largest to smallest
        max_idx = 0
        res = []
        
        for i in range(len(nums)):
            clean_deque(i)
            deq.append(i)
            if i >= k - 1: # only then starts adding to res
                res.append(nums[deq[0]])
        return res

s = Solution()
# s.maxSlidingWindow_optimized([1,3,-1,-3,5,3,6,7], 3)
s.maxSlidingWindow_optimized([7,6,5,4,3,5,6], 3)