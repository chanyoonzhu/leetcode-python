"""
- dynamic programming (0/n knapsack)
- O(n*t), O(t)
"""
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        
        dp = [""] * (target + 1)
        
        def combine(op1, c):
            i = 0
            while i < len(op1):
                if c >= op1[i]:
                    break
                i += 1
            return op1[:i] + c + op1[i:]
        
        def maxNum(n1, n2):
            len1, len2 = len(n1), len(n2)
            if len1 > len2:
                return n1
            elif len1 < len2:
                return n2
            else:
                i = 0
                while i < len1:
                    if n1[i] == n2[i]:
                        i += 1
                        continue
                    return n1 if n1[i] > n2[i] else n2
                            
        def findMax(prev, op1, c):
            if len(prev) > len(op1) + 1:
                return prev
            return maxNum(prev, combine(op1, c))

        # knapsack       
        for i, c in enumerate(cost):
            n = i + 1
            for j in range(target + 1 - c):
                if dp[j] or j == 0:
                    dp[j + c] = findMax(dp[j + c], dp[j], str(n))
        
        return dp[-1] if dp[-1] else "0"