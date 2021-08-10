"""
- dynamic programming (bottom-up): dp[i]: length of the longest subsequence ending at number i.
- O(n^2), O(n)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        N = len(nums)
        dp = [1] * N
        
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

"""
- monotonically-increasing array
- O(nlogn), O(n)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        selected = [] # best selection at each iteration i.
        for i in range(len(nums)):
            x = nums[i]
            if not selected or selected and x > selected[-1]:
                selected.append(x)
            else:
                i = bisect.bisect_left(selected, x)
                selected[i] = x
        return len(selected)