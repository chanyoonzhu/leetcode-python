    
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
        lefts, rights = [1], [1]
        
        for i in range(n):
            lefts.append(lefts[-1] * nums[i])
            rights.insert(0, rights[0] * nums[n-1-i])
        
        res = []
        for i in range(n):
            res.append(lefts[i] * rights[i+1])
        return res

"""
- space optimized (use res to store lefts, a variable to store accumulated rights)
- O(n), O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        right = 1
        for i in range(n - 1, -1, -1):
            right = right * nums[i + 1] if i < n - 1 else 1
            res[i] = res[i] * right
        
        return res
        