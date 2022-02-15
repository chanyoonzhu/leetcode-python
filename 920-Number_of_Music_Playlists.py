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
            # to speed up, can change above line to: if songs == list_size: return math.factorial(songs)
            if songs == 0 or songs > list_size: return 0 # no song to play or some song not played even once -> violates the rule
            # case 1: current pick is never played before, any song can be current pick so * songs
            ways = dp(songs - 1, list_size - 1) * songs % MOD
            # case 2: current pick is played before, current pick can choose from (song - k) songs
            if songs - k > 0:
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
                dp[gi][ni] = dp[gi-1][ni-1] * ni % MOD
                if ni > k: 
                    dp[gi][ni] = (dp[gi][ni] + dp[gi-1][ni] * (ni - k)) % MOD
        return dp[goal][n]