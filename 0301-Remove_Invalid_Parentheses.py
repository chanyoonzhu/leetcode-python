"""
- bfs
- O(n^3), O(n) ?
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        found = False
        result = []
        q = collections.deque([s])
        visited = set([s])
        while q:
            cur = q.popleft()
            if self.isValid(cur):
                result.append(cur)
                found = True
            if found: # stop appending any after found the first answer, only validate the rest in the queue
                continue
            for i in range(len(cur)):
                if cur[i] in ['(', ')']:
                    new = cur[:i] + cur[i + 1:]
                    if new not in visited:
                        visited.add(new)
                        q.append(new)
        return result
        
    def isValid(self, s):
        left_count = 0
        for c in s:
            if c == '(':
                left_count += 1
            elif c == ')':
                if not left_count:
                    return False
                else:
                    left_count -= 1
        return left_count == 0

"""
- backtracking with dfs
- O(2^n), O(2^n)
"""
class Solution:
    def removeInvalidParentheses(self, s):
        def dfs(i, left, right, removed, path):
            if i == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.result = set([path])
                    elif removed == self.min_removed:
                        self.result.add(path)
            elif s[i] == "(":
                dfs(i + 1, left, right, removed + 1, path) # remove
                dfs(i + 1, left + 1, right , removed, path + s[i]) # keep
            elif s[i] == ")":
                dfs(i + 1, left, right, removed + 1, path) # remove
                if left > right:
                    dfs(i + 1, left, right + 1, removed, path + s[i]) # keep
            else:
                dfs(i + 1, left, right, removed, path + s[i]) # skip
        
        self.result = set()
        self.min_removed = float("inf")
        dfs(0, 0, 0, 0, "")
        return self.result
        