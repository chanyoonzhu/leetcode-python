"""
- backtracking
- TLE
"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        res = []
        
        def backtracking(n, path):
            if n == 1:
                if len(path) > 1:
                    res.append(path)
            else:
                start = path[-1] if path else 2
                for factor in range(start, n + 1):
                    if n % factor == 0:
                        backtracking(n // factor, path + [factor])
        
        
        backtracking(n, [])
        return res

"""
- dfs
- intuition: recursively divide last item
 # [12] ---divide 12 by 2---> [2, 6]  ---divide 6 by 2---> [2, 2, 3] ---3 cannot divide 2 so done---
 # [12] ---divide 12 by 3---> [3, 4] (---divide 4 by 2---> [3, 2, 2])*
"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        res = []
        
        def dfs(divisor, path):
            last = path.pop()
            while divisor ** 2 <= last:
                new_last, mod = divmod(last, divisor)
                if mod == 0:
                    res.append(path + [divisor, new_last])
                    dfs(divisor, path + [divisor, new_last])
                divisor += 1  
        
        dfs(2, [n])
        return res