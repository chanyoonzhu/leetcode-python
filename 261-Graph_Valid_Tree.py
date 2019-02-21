import collections

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

        graph = collections.defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        
        visited = [False] * n
        
        def dfs(graph, n, prev, visited):
            visited[n] = True
            for nb in graph[n]:
                if nb != prev: # don't forget to use prev, can point to where it came from
                    if visited[nb]:
                        return False
                    else:
                        dfs(graph, nb, n, visited)
            return True
        
                
        if dfs(graph, 0, -1, visited):
            return sum(visited) == n
        return False
        

sl = Solution()
print(sl.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))