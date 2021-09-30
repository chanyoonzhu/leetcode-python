"""
- knapsack (2D)
- TLE
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    
        sum_p = sum(profit)
        sum_n = sum(group)
        prev_dp = [[0] * (sum_n + 1) for _ in range(sum_p + 1)]
        prev_dp[0][0] = 1
        for g, p in zip(group, profit):
            dp = [[0] * (sum_n + 1) for _ in range(sum_p + 1)]
            for i in range(sum_p + 1 - p):
                for j in range(sum_n + 1 - g):
                    if prev_dp[i][j]:
                        dp[i][j] += prev_dp[i][j] # not use current scheme
                        dp[i + p][j + g] += prev_dp[i][j] # use current scheme
            prev_dp = dp
        
        return sum([prev_dp[i][j] for i in range(len(prev_dp)) for j in range(len(prev_dp[i])) if i >= minProfit and j <= n]) % (10**9 + 7)

"""
- knapsack (2D)
- dp[i][j] means with i members and at least j profit, what is total schemes can be chosen.
- TLE
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(minProfit, -1, -1): # caveat: decrease to avoid over counting? 
                for j in range(n - g, -1, -1): # easy to miss: bound to n - g
                    dp[min(i + p, minProfit)][j + g] = (dp[min(i + p, minProfit)][j + g] + dp[i][j]) % (10**9 + 7) # smart use of min here!
        
        return sum(dp[minProfit]) % (10**9 + 7)