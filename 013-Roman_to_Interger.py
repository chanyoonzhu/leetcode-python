class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I': 1, 
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        
        res = 0
        prev = ''
        for c in s:
            if prev == 'I' and (c == 'V' or c == 'X'):
                res -= 2
            elif prev == 'X' and (c == 'L' or c == 'C'):
                res -= 20
            elif prev == 'C' and (c == 'D' or c == 'M'):
                res -= 200
            prev = c
            res += table[c]
            
        return res