"""
- dynamic programming (top-down)
- O(n^2), O(n)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        max_word_len = max(len(word) for word in words)
        
        @lru_cache(None)
        def dp(i):
            if i >= len(s):
                return True
            for k in range(i, min(len(s), i + max_word_len)):
                if s[i:k+1] in words and dp(k+1):
                    return True
            return False
        
        return dp(0)

"""
- dynamic programming (top-down)
- O(nw), O(n)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        def match(i, word):
            word_len = len(word)
            if i + word_len > N: return False
            for ii in range(word_len):
                if s[ii + i] != word[ii]:
                    return False 
            return True
        
        @lru_cache(None)
        def dfs(i):
            nonlocal N
            if i == N: return True
            for word in wordDict: # efficient when wordDict size is small
                if match(i, word) and dfs(i + len(word)):
                    return True
            return False
        
        return dfs(0)
   
"""
- dynamic programming (bottom-up)
- O(nw), O(n)
"""    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        
        for i in range(N):
            for w in wordDict:
                w_len = len(w)
                if i + 1 >= w_len and s[i + 1 - w_len:i + 1] == w and dp[i + 1 - w_len]:
                    dp[i + 1] = True
                    break
        return dp[-1]

"""
- Trie
- intuition: traverse s with only one trie in the pool, when meets a word, add a new trie to pool
- O(dict_len + w)
""" 
class Trie:
    def __init__(self):
        self.nodes= collections.defaultdict(Trie)
        self.isWord= False
        
    def addWord(self,word):
        current= self
        for c in word:
            current= current.nodes[c]    
        current.isWord= True
        

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root= Trie()
        for word in wordDict:
            root.addWord(word)
        
        tries= set([root])
        for c in s:
            tries= {trie.nodes[c] for trie in tries if c in trie.nodes} 
            if any(trie.isWord for trie in tries):
                tries.add(root)
        return any(trie.isWord for trie in tries)

s = "leetcode"
dic = ["leet", "code"]
sl = Solution()
print(sl.wordBreak(s, dic))
