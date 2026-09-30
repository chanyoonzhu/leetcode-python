"""
- array (linear scan)
- O(n), O(1)
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while i >= 0 and s[i] == ' ': # need to skip trailing ' '
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if words else 0