"""
- monotonically increasing stack
- O(n), O(n)
- similar problem: 402-Remove K Digits
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and stack[-1] > nums[i] and i - len(stack) <= n - 1 - k: # do not pop if not enough nums left in array
                stack.pop()
            if len(stack) < k: # don't add if have enough
                stack.append(nums[i])
        return stack