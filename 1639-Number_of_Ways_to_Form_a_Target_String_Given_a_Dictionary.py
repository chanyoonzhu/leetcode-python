"""
- Dynamic Programming
- TLE
"""
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        # c_to_match_pos example:
        # a -> [0, 3],[1, 3]
        # b -> [0, 1, 2, 3]
        # a -> [0, 3],[1, 3]
        
        MOD = 10 ** 9 + 7
        c_to_match_pos = defaultdict(list)
        chars = set(list(target))
        for word in words:
            word_c_to_match_pos = defaultdict(list)
            for i in range(len(word)):
                c_dict = word[i]
                if c_dict in chars:
                    word_c_to_match_pos[c_dict].append(i)
            for c_dict in word_c_to_match_pos:
                c_to_match_pos[c_dict].append(word_c_to_match_pos[c_dict])
        
        @lru_cache(None)
        def dp(i, x):
            if i == len(target):
                return 1
            c = target[i]
            positions = c_to_match_pos[c]
            ways = 0
            for pos_group in positions:
                idx = bisect.bisect_left(pos_group, x)
                for k in range(idx, len(pos_group)):
                    ways = (ways + dp(i + 1, pos_group[k] + 1)) % MOD
            return ways
        
        return dp(0, 0)

"""
- Dynamic Programming
- O(wm + nx)
"""
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(words[0]), len(target)
        char_at_idx_count = defaultdict(lambda: [0] * m)
        for word in words:
            for i, c in enumerate(word):
                char_at_idx_count[c][i] += 1  # Count the number of character `c` at index `i` of all words

        @lru_cache(None)
        def dp(i, x):
            if i == n: 
                return 1
            if x == m:  # Reached to length of words[x] but don't found any result
                return 0
            c = target[i]
            ans = dp(i, x + 1)  # Skip k_th index of words
            if char_at_idx_count[c][x] > 0: # Take k_th index of words if found character `c` at index k_th
                ans += dp(i + 1, x + 1) * char_at_idx_count[c][x]
                ans %= MOD
            return ans

        return dp(0, 0)