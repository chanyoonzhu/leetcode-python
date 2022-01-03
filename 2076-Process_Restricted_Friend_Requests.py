"""
- union find
- O(nk), O(n)
"""
class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 != p2:
            self.parents[p2] = p1

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        uf = UF(n)
        requests_len = len(requests)
    
        
        res = [True] * requests_len
        for i in range(requests_len):
            v1, v2 = requests[i]
            v1p, v2p = uf.find(v1), uf.find(v2)
            for x, y in restrictions:
                xp, yp = uf.find(x), uf.find(y)
                if set([v1p, v2p]) == set([xp, yp]): # cannot be connected when have same parents with restricted pair (connecting parents would connected the restricted pair)
                    res[i] = False
                    break
            if res[i]:
                uf.union(v1, v2)
        
        return res
        