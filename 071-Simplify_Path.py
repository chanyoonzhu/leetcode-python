"""
- stack (one-pass)
- intuition: ".." offsets a directory
- O(n), O(n)
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        part = ''
        for c in path + '/':
            if c != '/':
                part += c
            else:
                if part == '..':
                    if stack:
                        stack.pop()
                elif part and part != '.':
                    stack.append(part)    
                part = ''
        return '/' + '/'.join(stack)

"""
- stack (two-pass with split)
- O(n), O(n)
"""
class Solution(object):
    def simplifyPath(self, path):
        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)