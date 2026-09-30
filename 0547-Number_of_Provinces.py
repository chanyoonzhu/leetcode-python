"""
- O(n^2), O(n)
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()
        graph = defaultdict(set)
                
        N = len(isConnected)
        for i in range(N):
            for j in range(i+1, N):
                if isConnected[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)
        
        for i in range(N):
            if i not in visited:
                res += 1
                self._dfs(i, visited, graph)  # todo: dfs
        return res
    
    def _dfs(self, i, visited, graph):
        visited.add(i)
        for j in graph[i]:
            if j not in visited:
                self._dfs(j, visited, graph)
        