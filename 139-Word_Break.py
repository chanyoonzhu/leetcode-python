class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """
        - O(2^n) - O(2^n)
        - recursion with memoization
        
        def inDic(s, start, end, mem):
            thisS = s[start:end+1]
            if thisS in mem:
                return mem[thisS]
            if thisS in wordDict:
                mem[thisS] = True
                return True
            else:
                if len(thisS) == 1:
                    mem[thisS] = False
                    return False
                else:
                    for i in range(start, end + 1):
                        if inDic(s, start, i, mem) and inDic(s, i+1, end, mem):
                            mem[thisS] = True
                            return True
                        else:
                            mem[thisS] = False
                    return False
        
        words = set(wordDict)
        mem = {}
        return inDic(s, 0, len(s)-1, mem)
        """
        
        """
        - O(nm), O(n)
        - Dynamic Programming
        - dp[i] - s[:i+1] can be "breakable"
        - update function:
            - for any word in dictionary, if s[:i+1] is equals word or if s[i-len(word)+1:i+1] equals word and dp[i-len(word)] is True(s[:i-len(word)+1] breakable), dp[i] is True
        """
        dp = [False] * len(s)
        
        for i in range(len(dp)):
            for word in wordDict:
                if (dp[i-len(word)] or i-(len(word)-1) == 0) and s[i-len(word)+1:i+1] == word:
                    dp[i] = True
                    break
        return dp[-1]

# Questions: Does case matter?

s = "leetcode"
dic = ["leet", "code"]
sl = Solution()
print(sl.wordBreak(s, dic))
