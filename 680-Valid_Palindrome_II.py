"""
- two pointers - wrong answer: "ebcbbececabbacecbbcbe" -> should be "True" not "False"
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        removed = 0
        while l < r:
            if s[l] != s[r]:
                if removed:
                    return False
                else:
                    removed += 1
                    if s[l] == s[r - 1]:
                        r -= 1
                    elif s[l + 1] == s[r]:
                        l += 1
                    else:
                        return False
            l += 1
            r -= 1           
        return True

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
