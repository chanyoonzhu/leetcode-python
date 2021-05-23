"""
- dp: dp[i] - the longest length of valid parentheses which ends EXACTLY at i
- O(n), O(n)
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i, c in enumerate(s):
            if c == ')' and i >= 1:
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else dp[i - 1] + 2
        return max(dp) if dp else 0

"""
- stack: stack[-1] stores the beginning index of recent valid substring -1
- O(n), O(n)
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])
        return result

"""
- two passes
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        result = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
                if left == right:
                    result = max(result, left + right)
                elif right > left:
                    left = right = 0
        
        # covers cases: "(()"
        left = right = 0
        for c in s[::-1]:
            if c == ')':
                right += 1
            else:
                left += 1
                if left == right:
                    result = max(result, left + right)
                elif left > right:
                    left = right = 0
        
        return result