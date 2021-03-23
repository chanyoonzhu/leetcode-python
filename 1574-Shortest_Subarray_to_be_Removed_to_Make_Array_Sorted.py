class Solution:
    """
    - two pointers
    - algorithm:
    1. pick qualifying prefix and suffix
    2. merge prefix and suffix
    """
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)
        left, right = 0, n - 1
        
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        
        if left == n - 1: # whole array is sorted
            return 0
        
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        min_removed = min(right, n - left - 1) # worst scenario
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                min_removed = min(min_removed, j - i - 1)
                i += 1
            else:
                j += 1
        return min_removed