class Solution:
    """
    - dp: top down - dp[i][j] stores whether the specific half-sum j can be gotten from the first i numbers
    - simular to knapsack line by line
    - O(m*n), O(m*n)
    """
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(dp, n, subsum):
            if subsum == 0:
                return True
            if n == 0 or subsum < 0:
                return False
            if dp[n][subsum] != -1: return dp[n][subsum]
            dp[n][subsum] = dfs(dp, n-1, subsum) or dfs(dp, n-1, subsum - nums[n-1])
            return dp[n][subsum]
        
        subsum, mod = divmod(sum(nums), 2)
        if mod: return False
        
        dp = [[-1] * (subsum + 1) for _ in range(len(nums) + 1)]
        
        return dfs(dp, len(nums), subsum)
    
    """
    - dp: bottom up - dp[i][j] stores whether the specific half-sum j can be gotten from the first i numbers
    - simular to knapsack line by line
    - O(m*n), O(m*n)
    """
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
    - dp: bottom up - dp[i][j] stores whether the specific sum j can be gotten from the first i numbers
    - simular to knapsack line by line
    - O(m*n), O(m) - only needs dp[i-1] to calculate dp[i]
    """
    def canPartition(self, nums: List[int]) -> bool:
        subsum, mod = divmod(sum(nums), 2)
        if mod: return False
        
        dp = [True] + [False] * subsum
        
        for i in range(1, len(nums)):
            for j in range(subsum, nums[i-1] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i-1]]
        return dp[subsum]