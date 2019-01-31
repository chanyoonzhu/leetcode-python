class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        - O(n)
        - dfs
        - intuition: https://blog.csdn.net/fuxuemingzhu/article/details/82951771
        
        def dfs(graph, visited, i):
            if visited[i] == 1: # visited in a previous round of dfs
                return True
            if visited[i] == 2: # visited in this round of dfs
                return False
            visited[i] = 2 # mark this node visited in this round
            for nb in graph[i]:
                if not dfs(graph, visited, nb):
                    return False
            visited[i] = 1 # if all neighbors checked no cyle, mark visited in previous rounds
            return True
                    
        # create graph (adjacency list)
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
            
        visited = [0] * numCourses # 0 - not visited  1 - visited in previous rounds  2 - visited in this dfs round
        
        # for every node
        for i in range(numCourses):
            if not dfs(graph, visited, i):
                return False
        
        return True
        """
        
        """
        - BFS
        - intuition: the start node has to have 0 incoming. remove start node from graph (all its neighbors' incoming nodes -1) and do it recursively
        """
        import collections

        graph = collections.defaultdict(list)
        inNodes = [0] * numCourses
        
        for p in prerequisites:
            graph[p[1]].append(p[0])
            inNodes[p[0]] += 1
        
        q = []
        curr = -1
        for i in range(numCourses):
            for j in range(len(inNodes)):
                if inNodes[j] == 0:
                    curr = j
                    inNodes[j] = -1 # mark as visited
                    q.append(j)
            if len(q) == 0: # none of the nodes has incoming = 0
                return False
            neighbors = graph[q[0]]
            del q[0]
            for nb in neighbors:
                inNodes[nb] -= 1
        return True

sl = Solution()
print(sl.canFinish(3, [[1,0],[1,2],[0,1]]))