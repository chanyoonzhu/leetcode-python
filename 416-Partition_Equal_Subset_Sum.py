"""
- dynamic programming (top-down)
- O(n*s), O(n*s) - s is the sum
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        div, mod = divmod(sum(nums), 2)
        if mod: return False
        
        @lru_cache
        def dp(i, total):
            if i >= len(nums):
                return True if total == div else False
            for j in range(i, len(nums)):
                if dp(j + 1, total + nums[j]):
                    return True
            return False
        
        return dp(0, 0)
    
"""
- dp: bottom up - dp[i][j] stores whether the specific half-sum j can be gotten from the first i numbers
- simular to knapsack line by line
- O(m*s), O(m*s)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subsum, mod = divmod(sum(nums), 2)
        if mod: return False
        
        n, m = len(nums) + 1, subsum + 1
        dp = [[False] * m for _ in range(n)]
        dp[0][0] = True
        
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]
        return dp[n-1][m-1]
    
"""
- dynamic programming (bottom-up knapsack)
- O(n * s), O(s)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        div, mod = divmod(sum(nums), 2)
        if mod: return False
        
        dp = [True] + [False] * div
        for n in nums:
            for i in range(div - n, -1, -1): # decrease to avoid over-counting
                if dp[i]:
                    dp[i + n] = True
        return dp[-1]

"""
- dynamic programming (bottom-up knapsack) with set
- O(n * s), O(s)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        div, mod = divmod(sum(nums), 2)
        if mod: return False
        
        sums = set()
        sums.add(0)
        for n in nums:
            sums |= set([s + n for s in sums])
        return div in sums