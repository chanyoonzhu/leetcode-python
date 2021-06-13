"""
- similar question: 496. Next Greater Element I
"""

"""
- monotonically increasing stack
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
- monotonically increasing stack: small space improvement - save index in stack only
- O(n), O(n)
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n
        for i in list(range(n)) * 2:
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result