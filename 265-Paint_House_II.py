"""
- dynamic programming (bottom-up)
- O(nk^2), O(n)
"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        M, N = len(costs), len(costs[0])
        dp = costs[0]
        
        for i in range(1, M):
            new_dp = [float("inf")] * N 
            for j in range(N):
                for prev_j in range(N):
                    if j != prev_j:
                        new_dp[j] = min(new_dp[j], dp[prev_j] + costs[i][j])
            dp = new_dp
        return min(dp)

"""
- dynamic programming (bottom-up)
- O(nk), O(n)
"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        M, N = len(costs), len(costs[0])
        for i in range(1, M):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])
            for j in range(N):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])