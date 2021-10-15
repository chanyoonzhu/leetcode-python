"""
- dynamic programming (top-down)
- O(n*g), O(n*g)
"""
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def dp(songs, list_size):
            if songs == 0 and list_size == 0: return 1
            if songs == 0 or songs > list_size: return 0 # every song must be listened at least once, so songs > list_size
            # case 1: the last added one is new song, listen i - 1 songs with j - 1 different songs, then the last one is definitely new song with the choices of N - (j - 1).
            ways = dp(songs - 1, list_size - 1) * (n - (songs - 1)) % MOD
            if songs - k > 0: # can add old song to the last one
                # case 2: the last added one is an old song: listen i - 1 songs with j different songs, then the last one is definitely old song with the choices of j-k because k songs can't be chosed from j - 1 to j - k
                ways += dp(songs, list_size - 1) * (songs - k) % MOD
            return ways % MOD
        return dp(n, goal)

"""
- dynamic programming (bottom-up)
- dp[ni][gi] - Number of Music Playlists with length gi and ni unique songs
- O(n*g), O(n*g) - space can be optimized to O(n)
"""
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        
        for gi in range(1, goal + 1):
            for ni in range(1, n + 1):
                dp[gi][ni] = dp[gi-1][ni-1] * (n - (ni - 1)) % MOD
                if ni > k: 
                    dp[gi][ni] = (dp[gi][ni] + dp[gi-1][ni] * (ni - k)) % MOD
        return dp[goal][n]