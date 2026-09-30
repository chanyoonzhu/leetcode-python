"""
- dfs
- O(27 = 3 * 3 * 3) - O(1), O(1)
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def dfs(s, group, path):
            if not s and not group:
                res.append(path[1:]) # strip the first '.'
            if not s or not group:
                return
            if s[0] == '0':
                dfs(s[1:], group - 1, path + "." + s[:1])
                return
            dfs(s[1:], group - 1, path + "." + s[:1])
            if len(s) >= 2: # easy to miss: check length
                dfs(s[2:], group - 1, path + "." + s[:2])
            if len(s) >= 3 and int(s[:3]) <= 255:
                dfs(s[3:], group - 1, path + "." + s[:3])
        
        dfs(s, 4, '')
        return res