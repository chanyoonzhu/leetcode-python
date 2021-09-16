"""
- backtracking
"""
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        result = float("inf")
        
        def backtrack(total, idx):
            nonlocal result
            diff = abs(result - target)
            if abs(total - target) < diff:
                result = total
            elif abs(total - target) == diff:
                result = min(result, total)
            
            if idx == len(toppingCosts): return
              
            for n in range(3):
                backtrack(total + toppingCosts[idx] * n, idx + 1)
        
        for cost in baseCosts:
            backtrack(cost, 0)
        
        return result

"""
- Other solutioins: knapsack, set
"""
            
        