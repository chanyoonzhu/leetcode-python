    
"""
- precomputation
- O(n), O(n)
1) Construct a temporary array left[] such that left[i] contains product of all elements on left of arr[i] excluding arr[i].
2) Construct another temporary array right[] such that right[i] contains product of all elements on on right of arr[i] excluding arr[i].
3) To get prod[], multiply left[] and right[].
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left_prods = [1] * n
        right_prods = [1] * n
        for i in range(1, n):
            left_prods[i] = left_prods[i - 1] * nums[i - 1] # don't need to multiply the last num
            right_prods[n - i - 1] = right_prods[n - i] * nums[n - i] # don't need to multiply the last num
            
        for i in range(n):
            res[i] = left_prods[i] * right_prods[i]
            
        return res

"""
- space optimized
- O(n), O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        for i in range(n):
            res[i] = res[i - 1] * nums[i - 1] if i > 0 else 1
        
        right = 1
        for i in range(n - 1, -1, -1):
            right = right * nums[i + 1] if i < n - 1 else 1
            res[i] = res[i] * right
        
        return res
        