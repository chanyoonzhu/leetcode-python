"""
- dynamic programming (top-down)
- O(n^3), O(n^2)
"""
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        
        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0
            moves = float("inf")
            for k in range(l, r + 1):
                if arr[l] == arr[k]: # if num at l and k is same, then they can be removed without additional cost when removing nums between l+1 and k-1 
                    moves = min(moves, max(1, dp(l + 1, k - 1)) + dp(k + 1, r)) # easy to miss: still need 1 move if no number between l+1 and k-1, so max(1, dp(l + 1, k - 1))     
            return moves
        
        return dp(0, len(arr) - 1)

"""
- dynamic programming (bottom-up)
- O(n^3), O(n^2)
"""
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:

        N = len(arr)
        dp = [[0] * N for _ in range(N)]
        
        for diff in range(N):
            for l in range(N - diff):
                if diff == 0:
                    dp[l][l] = 1
                else:
                    r = l + diff
                    dp[l][r] = float("inf")
                    for k in range(l, r + 1):
                        if arr[l] == arr[k]:
                            dp[l][r] = min(dp[l][r], max(1, dp[l+1][k-1] if l < k else 0) + (dp[k+1][r] if k < r else 0))
        return dp[0][N-1]