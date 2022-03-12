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
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        chunks = path.split("/")
        for chunk in chunks:
            if chunk:
                if chunk == "..":
                    if stack:
                        stack.pop()
                elif chunk == ".":
                    continue
                else:
                    stack.append(chunk)
                    
        return "/" + "/".join(stack)