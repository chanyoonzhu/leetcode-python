class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        def findNext(visited, i, j, x, y):
            nexti = i + x
            nextj = j + y
            if nexti >= 0 and nexti < len(forest) and nextj >= 0 and nextj < len(forest[0]):
                if not visited[nexti][nextj] and forest[nexti][nextj] >= 1:
                    visited[nexti][nextj] = 1
                    return [1, nexti, nextj]
                else:
                    visited[nexti][nextj] = 1
                    return [0, nexti, nextj]
            else:
                return [0, nexti, nextj]
            
        
        def findRoute(si, sj, ei, ej):
            visited = [[0] * len(forest[i]) for i in range(len(forest))]
            visited[si][sj] = 1
            q = [[0,si,sj]]
            while q:
                dist, i, j = q[0]
                del q[0]
                # start is the end
                if i == ei and j == ej:
                    return dist
                nexts = [findNext(visited,i, j, 0, -1), findNext(visited,i, j, 0, 1), findNext(visited,i, j, 1, 0), findNext(visited,i, j, -1, 0)]
                for next in nexts:
                    if next[0]:
                        if next[1] == ei and next[2] == ej:
                            return dist + 1
                        else:
                            q.append([dist+1, next[1], next[2]])
            return -1           
                
        TreeInfo = [[forest[i][j], i, j] for i in range(len(forest)) for j in range(len(forest[i])) if forest[i][j] > 1]
        TreeInfo = sorted(TreeInfo, key=lambda x: x[0])
        start = [0, 0]
        totalDist = 0
        
        for tree in TreeInfo:
            dist = findRoute(start[0], start[1], tree[1], tree[2])
            if dist != -1:
                totalDist += dist
                start = [tree[1], tree[2]]
            else:
                return -1
        
        return totalDist

sl = Solution()
forest = [[1,2,3],[0,0,4],[7,6,5]]
print(sl.cutOffTree(forest))