"""
- dfs
- my solution: find path first, then count prob
"""
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return self.dfs(graph, 1, 0, target, t, 1)
    
    # returns the probability of ending at target at time t
    def dfs(self, graph, cur, prev, dest, time, prob):
        if time == 0:
            return prob if cur == dest else 0 # return 0 when ending at other node than target
        nei_counts = len(graph[cur]) - (1 if prev else 0)
        if cur == dest:
            return prob if nei_counts == 0 else 0 # return 0 when going past target node (when target has neighbors)
        if nei_counts == 0: # no way to go
            return 0
        prob *= 1.0 / nei_counts
        for nei in graph[cur]:
            if nei != prev:
                nei_prob = self.dfs(graph, nei, cur, dest, time-1, prob)
                if nei_prob > 0: # only return when prob > 0 (can reach target at time t)
                    return nei_prob
        return 0

"""
- dfs
- my solution: find path first, then count prob
"""
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(set)
        self.path = [] # path from start to target
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        self.findPath(graph, 1, target, [], set())
        
        cur, prob = 1, 1
        for _ in range(t):
            if graph[cur]: prob *= 1.0 / len(graph[cur])
            if self.path: graph[self.path[0]].remove(cur) # easy to miss: trim the path going backward
            if not self.path:
                if graph[cur]: # can go past target
                    return 0
                else:
                    return prob
            cur = self.path.pop(0)
        return prob if not self.path else 0 # return 0 if not reached path end
    
    def findPath(self, graph, u, v, path, visited):
        visited.add(u)
        if u == v:
            self.path = path
        for nei in graph[u]:
            if nei not in visited:
                self.findPath(graph, nei, v, path + [nei], visited)