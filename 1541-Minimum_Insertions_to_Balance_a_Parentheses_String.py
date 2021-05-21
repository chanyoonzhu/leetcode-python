"""
- stack (using counter)
- O(n), O(1)
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        opens = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                opens += 1
            else:
                if not opens:
                    result += 1
                else:
                    opens -= 1
                i += 1
                if i == len(s):
                    result += 1
                    break
                if s[i] != ')':
                    result += 1
                    i -= 1
            i += 1
        return result + 2 * opens