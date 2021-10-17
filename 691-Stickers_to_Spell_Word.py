"""
- backtracking
- TLE
"""
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        N, T = len(stickers), len(target)
        words = [set(list(s)) for s in stickers]
        
        def backtrack(i, repo, used):
            if i == T:
                return used
            c = target[i]
            min_used = float("inf")
            if repo[ord(c) - ord('a')] > 0:
                repo[ord(c) - ord('a')] -= 1
                min_used = backtrack(i + 1, repo, used)
                repo[ord(c) - ord('a')] += 1 # don't forget to track back
                return min_used
            min_used = float("inf")
            for j in range(N):
                if c in words[j]:
                    for cc in stickers[j]: repo[ord(cc) - ord('a')] += 1
                    min_used = min(min_used, backtrack(i, repo, used + 1))
                    for cc in stickers[j]: repo[ord(cc) - ord('a')] -= 1
            return min_used
        
        counts = backtrack(0, [0] * 26, 0)
        return counts if counts < float("inf") else -1

"""
- backtracking with pruning
- TLE
"""    
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        cnt, res, n = collections.Counter(target), float("inf"), len(target)  
        def dfs(i, repo, used):
            nonlocal res
            if i == n: res = min(res, used)
            elif repo[target[i]] >= cnt[target[i]]: # if current repo can support target
                dfs(i + 1, repo, used)
            elif used < res - 1: # pruning
                for s in stickers:
                    if target[i] in s:
                        for cc in s: repo[cc] += 1
                        dfs(i + 1, repo, used + 1)
                        for cc in s: repo[cc] -= 1
        dfs(0, collections.defaultdict(int), 0)
        return res < float("inf") and res or -1

"""
- backtracking with memoization
- 
""" 
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        M = len(stickers)
        mp = [[0] * 26 for _ in range(M)] 
        for i in range(M):
            for c in stickers[i]:
                mp[i][ord(c) - ord('a')] += 1    
        dp = {}
        dp[""] = 0
        
        def helper(dp, mp, target):
            if target not in dp:
                # n = len(mp)
                tarCounts = [0] * 26
                for c in target:
                    tarCounts[ord(c) - ord('a')] += 1   
                ans = float("inf")
                for i in range(M): # iterate through stickers
                    if mp[i][ord(target[0]) - ord('a')] == 0: #target[0] not in sticker
                        continue
                    s = ''
                    for j in range(26):
                        if tarCounts[j] > mp[i][j]:
                            s += chr(ord('a') + j) * (tarCounts[j] - mp[i][j]) #s has all missing letters from target that cannot covered by current sticker
                    tmp = helper(dp, mp, s)
                    if (tmp != -1): 
                        ans = min(ans, 1 + tmp)    
                dp[target] = -1 if ans == float("inf") else ans
            return dp[target]

"""
- dynamic programming (knapsack 0/n)
- similar: 322-Coin Change
"""
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        bits =  1 << n
        dp = [float("inf")] * bits
        dp[0] = 0
        
        # bitmask - current target represented in bit ('0'/'1' - char non-exists/exists at target[i])
        for bitmask in range(bits):
            if dp[bitmask] < float("inf"):
                for sticker in stickers:
                    state = bitmask
                    for c in sticker:
                        for r in range(n):
                            pos = 1 << r
                            if target[r] == c and (pos & state) == 0: # char at target[r] not exist yet
                                state |= pos
                                break # can only use a sticker once at a time
                    dp[state] = min(dp[state], dp[bitmask] + 1) # state that can be reached after using current sticker
        result = dp[bits-1]
        return result if result < float("inf") else -1