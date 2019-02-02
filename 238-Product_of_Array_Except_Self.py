class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        """
        1) Construct a temporary array left[] such that left[i] contains product of all elements on left of arr[i] excluding arr[i].
        2) Construct another temporary array right[] such that right[i] contains product of all elements on on right of arr[i] excluding arr[i].
        3) To get prod[], multiply left[] and right[].
        """
        
        n = len(nums)
        left = [1] * n
        right = [1] * n
        prod = [1] * n
        
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
            
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        
        for i in range(n):
            prod[i] = left[i] * right[i]
        
        return prod
        