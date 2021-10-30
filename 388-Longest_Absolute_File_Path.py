"""
- stack
- O(n), O(n)
"""
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        curlen, maxlen = 0, 0
        stack = []
        for s in input.split('\n'):
            dir_len = len(s.lstrip('\t'))
            depth = s.count('\t')
            while len(stack) > depth:
                curlen -= stack.pop()
            stack.append(dir_len + 1)
            curlen += stack[-1]
            if '.' in s:
                maxlen = max(maxlen, curlen - 1)
        return maxlen

"""
- hashmap
- O(n), O(n)
"""
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        result = 0
        level_to_len = {0: 0}
        
        for line in input.split("\n"):
            dir_len = len(line.lstrip("\t"))
            level = len(line) - dir_len
            if '.' in line:
                result = max(result, level_to_len[level] + dir_len)
            else:
                level_to_len[level+1] = level_to_len[level] + dir_len + 1
        return result