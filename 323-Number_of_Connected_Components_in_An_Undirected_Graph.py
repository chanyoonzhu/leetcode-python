class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents = [i for i in range(n)]
        ranks = [0] * n
        components = n
        
        for e in edges:
            if self.find(parents, e[0]) == self.find(parents, e[1]):
                continue
            else:
                self.union(parents, ranks, e[0], e[1])
                components -= 1 # components subtract 1 every time two groups union
        
        return components
        
        
    def find(self, parents, i):
        if parents[i] != i:
            parents[i] = self.find(parents, parents[i])
        return parents[i]
            

    def union(self, parents, ranks, u, v):
        parentU = self.find(parents, u)
        parentV = self.find(parents, v)
        
        if ranks[parentU] > ranks[parentV]:
            parents[parentV] = parentU
        elif ranks[parentU] < ranks[parentV]:
            parents[parentU] = parentV
        else:
            ranks[parentU] += 1
            parents[parentV] = parentU

print(Solution().countComponents(4,
[[0,1],[2,3],[1,2]]))