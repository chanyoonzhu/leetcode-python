"""
- dynamic programming
- TLE
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        N = len(piles)
        
        @lru_cache(None)
        def dp(i, m):
            nonlocal N
            if i >= N: return 0
            maxx = 0
            for xa in range(1, 2 * m + 1): # greedily find x for Alice (xa) that maximize Alex's yield
                m_next = max(xa, m)
                minn = float("inf")
                for xb in range(1, 2 * m_next + 1): # greedily find x for Bob (xb) that minimize Alex's yield
                    minn = min(minn, dp(i + xa + xb, max(xb, m_next)))
                maxx = max(maxx, sum(piles[i: i + xa]) + minn)  # sun() part can be optimized with prefix sum
            return maxx

"""
- https://leetcode.com/problems/stone-game-ii/discuss/793881/python-DP-Thought-process-explained
- todo: bottom-up
"""