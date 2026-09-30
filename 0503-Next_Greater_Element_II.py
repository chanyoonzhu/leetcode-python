"""
- similar question: 496. Next Greater Element I
- difference: circular, numbers not unique
"""

"""
- brute force
- O(n^2), O(1)
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = []
        
        for i in range(n):
            x = nums[i]
            greater_found = False
            for ii in range(n):
                j = (i + ii) % n
                if nums[j] > x:
                    greater_found = True
                    res.append(nums[j])
                    break
            if not greater_found:
                res.append(-1)
        return res

"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n
        for i, num in enumerate(nums * 2):
            while stack and num > stack[-1][0]:
                _, pop_i = stack.pop()
                result[pop_i] = num
            if i < n:
                stack.append((num, i))
        return result

"""
- monotonically decreasing stack: small space improvement - save index in stack only
- O(n), O(n)
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        stack = [] # mono-decreasing
        res = [-1] * N
        
        for i in range(N * 2): # for circular
            idx = i % N
            while stack and nums[idx] > nums[stack[-1]]:
                res[stack.pop()] = nums[idx]
            stack.append(idx)
        return res