"""
- backtrack / dynamic programming (knapsack)
- O(n^2 + 2^n + w)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
                
        def match(i, word):
            return word == s[i:min(len(s), i+len(word))] # or s[i:].startswith(word):
        
        def dp(i, paths):
            if i == len(s):
                return paths
            next_paths = []
            for word in wordDict:
                if match(i, word):
                    next_paths.extend(dp(i + len(word), [path + [word] for path in paths]))
            return next_paths
                    
        paths = dp(0, [[]])
        return [" ".join(path) for path in paths]

"""
- similar
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        N = len(s)
        res = []
        
        @lru_cache(None)
        def dp(i, path):
            if i == len(s):
                res.append(path.lstrip())
            for word in words:
                if s[i:i+len(word)] == word:
                    dp(i+len(word), path + " " + word)
                    
                    
        dp(0, "")
        return res