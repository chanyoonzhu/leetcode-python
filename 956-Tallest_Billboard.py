
"""
- dynamic programming (top-down)
- TLE
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
    
        @lru_cache(None)
        def dp(i, l1, l2):
            if i == -1:
                return l1 if l1 == l2 else 0
            return max(dp(i - 1, l1, l2), dp(i - 1, l1 + rods[i], l2), dp(i - 1, l1, l2 + rods[i]))
        
        return dp(len(rods) - 1, 0, 0)

"""
- dynamic programming (top-down) - knapsack (two bags)
- TLE
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        max_height = sum(rods)

        dp = [[False] * (max_height + 1) for _ in range(max_height + 1)]
        dp[0][0] = True
        
        for h in rods:
            for l in range(max_height - h, -1, -1):
                for r in range(max_height - h, -1, -1):
                    dp[l+h][r] |= dp[l][r]
                    dp[l][r+h] |= dp[l][r]
        
        for l in range(max_height, -1, -1):
            for r in range(max_height, -1, -1):
                if l == r and dp[l][r]:
                    return l
        return 0

"""
- dynamic programming (top-down) - knapsack (one bag)
- O(n * sum(rods)), O(n * sum(rods))
- intuition: Given a list of numbers, multiply each number with 1 or 0 or -1, make the sum of all numbers to 0. Find a combination which has the largest sum of all positive numbers
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, diff): # i - rod index; diff - diff b/t shorter and longer beam; dp[i][diff] max shorter beam length
            
            if i == len(rods):
                return 0 if diff == 0 else float("-inf")
            
            rod_len = rods[i]
            # max of (add to longer beam, add to longer beam, do not add)
            return max(dp(i + 1, diff + rod_len), rod_len + dp(i + 1, diff - rod_len), dp(i + 1, diff))
        
        return dp(0, 0)

"""
- dynamic programming - knapsack 
- dp[i] - the largest sum of all positive numbers for subsequence with sum equal to i
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        prev_dp = dict()
        prev_dp[0] = 0
        
        for n in rods:
            dp = collections.defaultdict(int)
            for s in prev_dp:
                dp[s + n] = max(prev_dp[s] + n, dp[s + n])
                dp[s] = max(prev_dp[s], dp[s])
                dp[s - n] = max(prev_dp[s], dp[s - n])
            prev_dp = dp
        return dp[0]  # the largest sum of all positive numbers for subsequence with sum equal to 0
    
    

