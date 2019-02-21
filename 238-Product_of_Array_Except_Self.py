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
        
        res = [0] * len(nums)
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
            rightProduct[len(nums)-i-1] = rightProduct[len(nums)-i] * nums[len(nums)-i]
        
        for i in range(len(nums)):
            res[i] = leftProduct[i] * rightProduct[i]
            
        return res
        