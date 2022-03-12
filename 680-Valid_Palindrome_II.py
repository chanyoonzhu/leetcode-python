"""
- two pointers
- O(n), O(1)
"""
class Solution:
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.validPalindromeUtil(s, l + 1, r) or self.validPalindromeUtil(s, l, r - 1)
        return True
    
    def validPalindromeUtil(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

"""
- recursive
- O(n), O(n)
"""
class Solution:
    def validPalindrome(self, s):
        return self.palindromHelper(s)
    
    def palindromHelper(self, s, has_removed=False):
        if not s or len(s) == 1:
            return True
        if s[0] == s[-1]:
            return self.palindromHelper(s[1:-1], has_removed)
        if s[0] != s[-1]:
            if has_removed:
                return False
            return self.palindromHelper(s[1:], True) or self.palindromHelper(s[:-1], True)
