"""
- String
- find the longest palindrome that begin with the first char
- O(n^2), O(n)
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        N = len(s) 
        for i in range(N // 2, -1, -1):
            left = s[:i+1]
            # key: need to match even palindrome first to get the longest palindrome beginning with first char (eg. "aabba" -> "aa", not "a")
            if s[i+1:].startswith(left[::-1]): # even palindrome
                return s[2*len(left):N][::-1] + s
            if s[i:].startswith(left[::-1]): # odd palindrome
                return s[2*len(left)-1:N][::-1] + s

"""
- todo: KMP
"""
        