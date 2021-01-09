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
        for i in range(len(stack)-1, -1, -1):
            del s_list[i]
        return "".join(s_list)

s = Solution()
s.minRemoveToMakeValid("())()(((")