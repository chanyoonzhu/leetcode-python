"""
- memorizing smallest nums[i]
- O(n^2), O(1)
- time limit exceeded
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_i = inf
        for j in range(n - 1):
            min_i = min(min_i, nums[j])
            for k in range(j + 1, n):
                if min_i < nums[k] < nums[j]:
                    return True
        return False

"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k_value = float("-inf")
        for n in nums[::-1]:
            if n < k_value: # i_value found
                return True
            while stack and stack[-1] < n:
                k_value = stack.pop() # guaranteed largest k_value found when n is the current j_value
            stack.append(n)
        return False