"""
- dfs
"""
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list) # max key size: 50
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        ans = [-1] * len(nums)
        path = collections.defaultdict(list) # val -> list of (pos, depth)
        seen = {0}
        
        def dfs(i, d):  # d - depth in tree
            """Populate ans via dfs."""
            dd = -1 
            for x in path:
                if gcd(nums[i], x) == 1:
                    if path[x] and path[x][-1][1] > dd: # use largest depth
                        ans[i] = path[x][-1][0]
                        dd = path[x][-1][1]
                        
            path[nums[i]].append((i, d))
            for ii in graph[i]: 
                if ii not in seen: 
                    seen.add(ii)
                    dfs(ii, d + 1)
            path[nums[i]].pop()
            
            
        dfs(0, 0)
        return ans