"""
- union find - my solution
- TLE
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        islands = list()
        visited = set()        
        
        for x, y in positions:
            should_join = set()
            for i, island in enumerate(islands):
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), ()]:
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) in island:
                        should_join.add(i)
                        island.add((x, y))
            if not should_join:
                islands.append(set([(x, y)]))
            else:
                joined = set().union(*[island for i, island in enumerate(islands) if i in should_join])
                new_islands = [island for i, island in enumerate(islands) if i not in should_join]
                new_islands.append(joined)
                islands = new_islands
            result.append(len(islands))
        return result

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        table = {}
        res = []
        total = 0
        parents = [[[]] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                parents[i][j] = [i,j]
        ranks = [[0] * n for _ in range(m)]
        
        def find(position, parents):
            i, j = position[0], position[1]
            if parents[i][j] != position:
                parents[i][j] = find(parents[i][j], parents)
            return parents[i][j]
        
        def union(p1, p2, parents, ranks):
            parent1 = find(p1, parents)
            parent2 = find(p2, parents)
            
            if ranks[parent1[0]][parent1[1]] < ranks[parent2[0]][parent2[1]]:
                parents[parent1[0]][parent1[1]] = parent2
            elif ranks[parent1[0]][parent1[1]] > ranks[parent2[0]][parent2[1]]:
                parents[parent2[0]][parent2[1]] = parent1
            else:
                ranks[parent1[0]][parent1[1]] += 1
                parents[parent2[0]][parent2[1]] = parent1

        def findAdjacentIslands(position, table):
            res = []
            i, j = position[0], position[1]
            if (i-1,j) in table:
                res.append([i-1,j])
            if (i+1,j) in table:
                res.append([i+1,j])
            if (i,j+1) in table:
                res.append([i,j+1])
            if (i,j-1) in table:
                res.append([i,j-1])
            return res
        
        for position in positions:
            adjacentIslands = findAdjacentIslands(position, table)
            if not adjacentIslands:
                total += 1
            else:
                if position == [0,0]: x = 2
                parents[position[0]][position[1]] = parents[adjacentIslands[0][0]][adjacentIslands[0][1]]
                merged = 0
                for i in range(1, len(adjacentIslands)):
                    if find(adjacentIslands[i-1], parents) != find(adjacentIslands[i], parents): # bs: sometimes 2 adjacent belong to the same islands!
                        merged += 1    
                        union(adjacentIslands[i-1], adjacentIslands[i], parents, ranks)
                total -= merged
            res.append(total)
            table[(position[0], position[1])] = 1
            
        return res

print(Solution().numIslands2(3,3,[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]))