"""
- two passes: remove ')' in the first pass and '(' in the second pass
- O(n), O(1)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
    
        s_list = list(s)
        opens = 0
        i = 0
        while i < len(s_list):
            if s_list[i] == '(':
                opens += 1
            elif s_list[i] == ')':
                if opens:
                    opens -= 1
                else:
                    del s_list[i]
                    i -= 1
            i += 1
        
        closes = 0
        i = len(s_list) - 1
        while i >= 0:
            if s_list[i] == ')':
                closes += 1
            elif s_list[i] == '(':
                if closes:
                    closes -= 1
                else:
                    del s_list[i]
            i -= 1
        
        return ''.join(s_list)

class Solution(object):
    """
    - stack
    - O(n), O(n): could have up to n characters in stack
    """
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s_list = list(s)
        i = 0
        while i < len(s_list):
            if s_list[i] == "(":
                stack.append(i)
            elif s_list[i] == ")":
                if stack:
                    stack.pop()
                else:
                    del s_list[i]
                    i -= 1
            i += 1             
        for i in stack[::-1]:
            del s_list[i]
        return "".join(s_list)

s = Solution()
s.minRemoveToMakeValid("())()(((")