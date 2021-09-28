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
- dp (bottom-up): 0/1 knapsack
- O(n*S), O(S)
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        N = len(stones)
        prev_dp = set([stones[0], -stones[0]])
        for i in range(1, N):
            """
            or:
            dp = set([n + stones[i] for n in dp]) | set([n - stones[i] for n in dp])
            """
            dp = set() 
            for n in prev_dp:
                dp.add(n + stones[i])
                dp.add(n - stones[i])
            prev_dp = dp
        return min([n for n in prev_dp if n >= 0])
                
            
            
                        
                