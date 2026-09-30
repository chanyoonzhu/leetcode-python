"""
- monotonically increasing stack:
- O(n), O(n)
- similar problem: 1673-Find the Most Competitive Subsequence
"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        stack = []
        for i, d in enumerate(num):
            while stack and stack[-1] > d and i - len(stack) < k:
                stack.pop()
            if n - len(stack) > k:
                stack.append(d)
        return ''.join(stack).lstrip('0') or '0' # get rid of leading zeroes

s = Solution()
print(s.removeKdigits('1234567890', 9))
        
            