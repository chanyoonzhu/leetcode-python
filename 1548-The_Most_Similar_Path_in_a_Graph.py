class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        m = len(targetPath)
        
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        path_prev = [[0] * n for _ in range(m)] # for recording path
        dp = [[m] * n for _ in range(m)]
        for v in range(n):
            dp[0][v] = (names[v] != targetPath[0])
            
        # dp
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i-1][u] < dp[i][v]: # choose min edit distance for i-1
                        dp[i][v] = dp[i-1][u]
                        path_prev[i][v] = u # record path
                dp[i][v] += (names[v] != targetPath[i]) # add edit distance at i
                
        # build path
        path, min_dist = [0], m
        for v in range(n):
            if dp[-1][v] < min_dist:
                min_dist = dp[-1][v]
                path[0] = v
        for i in range(m - 1, 0, -1):
            u = path_prev[i][path[-1]]
            path.append(u)
            
        return path[::-1]        