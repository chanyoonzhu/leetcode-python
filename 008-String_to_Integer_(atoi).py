"""
- String
- O(n), O(1)
"""
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = list(str.strip())
        if len(l) == 0:
            return 0
        
        sign = 1
        i = 0
        if l[0] in ['-', '+']:
            sign = -1 if l[0] == '-' else 1
            i = 1
        
        val = 0
        
        while i < len(l) and l[i].isdigit():
            val = val * 10 + ord(l[i]) - ord('0')
            i += 1
        
        return max(-2**31, min(2**31 - 1, val * sign))