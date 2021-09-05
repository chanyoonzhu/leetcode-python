"""
- dynamic programming (bottom-up) dp[n] - probability to reach number n 
- TLE
"""
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        if k == 0 or k - 1 + maxPts <= n: # easy to miss: cannot draw, or cannot be larger than n
            return 1
        
        dp = [1] + [0] * n
        for cur_p in range(1, n + 1):
            for p in range(1, maxPts + 1):
                if 0 <= cur_p - p < k: # easy to miss < k (when reach k, cannot draw card any more)
                    dp[cur_p] += dp[cur_p - p] * 1.0 / maxPts       
        return sum(dp[k:]) # easy to miss: final points have to be larger than k

"""
- dynamic programming + sliding window running sum
- O(n), O(n)
"""
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        if k == 0 or k - 1 + maxPts <= n: # easy to miss: cannot draw, or cannot be larger than n
            return 1
        
        dp = [1] + [0] * n
        last_p_probs_total = 1
        for cur_p in range(1, n + 1):
            dp[cur_p] = last_p_probs_total * 1.0 / maxPts
            if cur_p >= maxPts: last_p_probs_total -= dp[cur_p - maxPts]
            if cur_p < k: last_p_probs_total += dp[cur_p]      
        return sum(dp[k:])