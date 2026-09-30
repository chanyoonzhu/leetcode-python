"""
- O(n^3), O(n^3)
- pick all possible starting and ending positions for a substring, and verify if it is a palindrome.
- TLE
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(t):
            reverse = t[::-1]
            return t == reverse
        
        longestLen = currLen = 0
        start = end = 0
        for i in range(len(s)):
            for k in range(len(s), i, -1):
                if isPalindrome(s[i:k]):
                    currLen = k - i
                    if currLen > longestLen:
                        longestLen = currLen
                        start, end = i, k
                    break #others starting at the same index position cannot be longer than this one
        return s[start:end]
            
"""
- dynamic programming (top-down)
- dp(i, j): is s[i:j+1] a palindrome
- O(n^2), O(n^2)
- MLE
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        @lru_cache(None)
        def isPalindrome(i, j):
            if i == j:
                return True
            if i + 1 == j and s[i] == s[j]:
                return True
            return s[i] == s[j] and isPalindrome(i+1, j-1)
        
        longest = 0
        res = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    if j - i + 1 > longest:
                        longest = max(longest, j - i + 1)
                        res = s[i:j+1]
        return res

"""
- Dynamic Programming (bottom-up)
- dp[i][j] keeps track of whether s[i:j+1] is a palindrome
- O(n^2), O(n^2)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[0] * len(s) for _ in range(len(s))]
        max_len = 0
        start = end = 0
            
        for i in range(len(s)-1, -1, -1): # starting from bottom right corner
            for j in range(i, len(s)): 
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start, end = i, j + 1
        
        return s[start:end]
        
        
"""
- starting from the middle
- O(n^2), O(n^2)
"""
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        res = ""
        for i in range(len(s)):
            odd_longest = self.findLocalPalindrome(s, i, i)
            if len(odd_longest) > len(res):
                res = odd_longest
            even_longest = self.findLocalPalindrome(s, i, i+1)
            if len(even_longest) > len(res):
                res = even_longest
        return res
    
    def findLocalPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

""""
O(n), O(1)
- Manache's Algorithm (using mirror feature of a palindrome)
- not finished
"""
