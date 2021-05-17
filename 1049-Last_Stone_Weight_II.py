"""
- dp (top-down dfs):
- O(n^n)
- time limit exceeded
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if not stones: return 0
        if len(stones) == 1: return stones[0]
        n = len(stones)
        min_weight = float("inf")
        for i, weight_i in enumerate(stones):
            for j in range(i + 1, n):
                diff = abs(weight_i - stones[j])
                if not diff:
                    new_stones = stones[:i] + stones[i + 1:j] + stones[j + 1:]
                else:
                    new_stones = stones[:i] + [diff] + stones[i + 1:j] + stones[j + 1:]
            min_weight = min(min_weight, self.lastStoneWeightII(new_stones))
        return min_weight

"""
- dp (top-down dfs): 0/1 knapsack
- intuition: have to divide all nums into two bags, then the possible min diff between them is our answer. 
One of the bag sums has to be <= _sum // 2, we calculate the maximum possible that can fit into that bag (bag 1), 
and then calculate answer using sum(bag_2) - sum(bag1), which is sum(nums) - 2 * sum(bag1)
- O(n*S), O(n)
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, _sum = len(stones), sum(stones)
        dp = [[0] * (_sum // 2 + 1) for _ in range(n)] # dp[i][s] means the max value of putting the first i number into a backpack with a maximum capacity of s
        
        def dfs(i, total):
            if total == 0 or i < 0: return 0
            if dp[i][total]: return dp[i][total]
            if stones[i] > total: # cannot take stone[i]
                dp[i][total] = dfs(i - 1, total)
            else:
                dp[i][total] = max(dfs(i - 1, total), dfs(i - 1, total - stones[i]) + stones[i]) # max of 1. not taking stone[i] and 2. taking stone[i]
            return dp[i][total]
        
        return _sum - 2 * dfs(n - 1, _sum // 2) # = sum(list_1) + sum(list_2) - 2 * sum(list_1)

"""
- dp (bottom-up): dp[i][j] means the max value of putting the first i number into a backpack with capacity of j
- O(n*S), O(n)
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, _sum = len(stones), sum(stones)
        dp = [[0] * (_sum // 2 + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(_sum // 2 + 1):
                if j < stones[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])
        return _sum - 2 * dp[n][_sum // 2] 
"""
- dp (bottom-up):
- O(n*S), O(1)
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, _sum = len(stones), sum(stones)
        dp = [0] * (_sum // 2 + 1) # dp[j] means the max value of putting the numbers into a backpack with capacity of j
        for n in stones:
            for j in range(_sum // 2, n - 1, -1):
                dp[j] = max(dp[j], dp[j - n] + n)
        
        return _sum - 2 * dp[_sum // 2]
                
            
            
                        
                