"""
- BFS with greedy (greedily color all neighbors)
- O(N + E), O(N)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        for node in range(len(graph)): # caveat: need to iterate through all node since the graph may not be connected
            if node not in visited:
                q = [node]
                visited[node] = True
                while q:
                    cur_node = q.pop()
                    for neighbor in graph[cur_node]:
                        if neighbor not in visited:
                            visited[neighbor] = not visited[cur_node]
                            q.append(neighbor)
                        elif visited[neighbor] == visited[cur_node]:
                            return False
        return True

"""
- DFS with greedy
- O(N + E), O(N)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor in visited:
                    if visited[neighbor] == visited[node]:
                        return False
                else:
                    visited[neighbor] = not visited[node]
                    if not dfs(neighbor): return False
            return True         
        
        for node in range(len(graph)):
            if node not in visited:
                visited[node] = True
                if not dfs(node): return False   
        return True