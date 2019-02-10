class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        """
        - tree: all nodes are connected, no cycle
        """
        def dfs(node, prev):
            if visited[node]:
                return False
            else:
                visited[node] = True
                for nb in graph[node]:
                    if nb != prev and not dfs(nb, node):
                        return False
                return True
        
        graph = collections.defaultdict(list)
        nodes = set([i for i in range(n)])
        visited = [False] * n
        
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        if not dfs(0, -1): return False
        for val in visited:
            if not val:
                return False
        return True
        

sl = Solution()
print(sl.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))