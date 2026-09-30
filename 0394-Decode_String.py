"""
- dfs
"""
class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(i, j):
            if i > j: return ""
            if not s[i].isdigit():
                return s[i] + helper(i + 1, j)
            num = 0
            while s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            ii = i + 1
            opens = 1
            while opens: # find next matching closing brackets
                if s[ii] == ']': opens -= 1
                if s[ii] == '[': opens += 1
                ii += 1
            return num * helper(i + 1, ii - 2) + helper(ii, j)
        
        return helper(0, len(s) - 1)


"""
- stack
- O(n), O(n)
"""
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        substr = ""
        for c in s:
            if c.isdigit():
                if stack and stack[-1].isdigit():
                    stack[-1] += c
                else:
                    stack.append(c)
            elif c == '[':
                stack.append(c)
            elif c == ']':
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()
                num = int(stack.pop())
                stack.append(num * substr)
                substr = ""
            else:
                stack.append(c)
        
        return ''.join(stack)