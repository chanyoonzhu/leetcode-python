"""
- dynamic programming (top-down)
- (len(group)*n*minProfit)
- TLE
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        profitGroupPairs = list(zip(profit, group))
        
        @lru_cache(None)
        def dp(i, p, g):
            if g > n:
                return 0
            if p < minProfit and i < 0: return 0 # or if minProfit - p > profit_sums[i+1]: return 0
            if i < 0:
                return 1
            cur_p, cur_g = profitGroupPairs[i]
            return dp(i - 1, p + cur_p, g + cur_g) + dp(i - 1, p, g) # either choose crime i or not
        
        return dp(len(profitGroupPairs) - 1, 0, 0)

"""
- knapsack (2 bags)
- dp[i][j]: with i members and j profit, what is total schemes can be chosen.
- TLE
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        profit_max = sum(profit)
        profitGroupPairs = list(zip(profit, group))
        N = len(profitGroupPairs)
        MOD = 10**9 + 7
        
        dp = [[0] * (n + 1) for _ in range(profit_max + 1)]
        dp[0][0] = 1
        for cur_p, cur_g in profitGroupPairs:
            for p in range(profit_max - cur_p, -1, -1):
                for g in range(n - cur_g, -1, -1):
                    dp[p + cur_p][g + cur_g] = (dp[p + cur_p][g + cur_g] + dp[p][g]) % MOD
        return sum([sum(dp[p]) for p in range(profit_max + 1) if p >= minProfit]) % MOD

"""
- knapsack (2 bags)
- dp[i][j] means with i members and at least j profit, what is total schemes can be chosen.
- TLE
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    
        profitGroupPairs = list(zip(profit, group))
        N = len(profitGroupPairs)
        MOD = 10**9 + 7
        
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1
        for cur_p, cur_g in profitGroupPairs:
            for p in range(minProfit, -1, -1):
                for g in range(n - cur_g, -1, -1):
                    dp[min(minProfit, p + cur_p)][g + cur_g] = (dp[min(minProfit, p + cur_p)][g + cur_g] + dp[p][g]) % MOD # key: min
        return sum(dp[minProfit]) % MOD