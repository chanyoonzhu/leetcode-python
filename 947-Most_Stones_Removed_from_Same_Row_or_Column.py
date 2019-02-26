import collections;

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        """
        - O(mn), O(mn)
        - dfs

        if not stones:
            return 0
        
        totalRegion = 0
        table0 = collections.defaultdict(list)
        table1 = collections.defaultdict(list)
        unVisited = set([tuple(s) for s in stones])
        
        for s in stones:
            table0[s[0]].append(s[1])
            table1[s[1]].append(s[0])
            
        while unVisited:
            stone = unVisited.pop()
            q = [stone]
            while q:
                row, col = q.pop(0)
                for nbCol in table0[row]:
                    if nbCol != col and (row, nbCol) in unVisited:
                        q.append((row, nbCol))
                        unVisited.remove((row, nbCol))
                for nbRow in table1[col]:
                    if nbRow != row and (nbRow, col) in unVisited:
                        q.append((nbRow, col))
                        unVisited.remove((nbRow, col))
                        
            totalRegion += 1
            
        return len(stones) - totalRegion
        """

        table0 = collections.defaultdict(list)
        table1 = collections.defaultdict(list)
        tableStones = {}
               
        parents = [i for i in range(len(stones))]
        ranks = [0] * len(stones)
        distinctParents = set()
        
        for i, s in enumerate(stones):
            table0[s[0]].append(s[1])
            table1[s[1]].append(s[0])
            tableStones[tuple(s)] = i
            
        for i in range(len(stones)):
            row, col = stones[i]
            for nbCol in table0[row]:
                if nbCol != col:
                    self.union(parents, ranks, tableStones[(row, nbCol)], i)
            for nbRow in table1[col]:
                if nbRow != row:
                    self.union(parents, ranks, tableStones[(nbRow, col)], i)
                    
        for i in range(len(stones)):
            parent = self.find(parents, i)
            distinctParents.add(parent)
            
        return len(stones) - len(distinctParents)
        
    def find(self, parents, item):
        if parents[item] != item: # df: if, not while!
            parents[item] = self.find(parents, parents[item])
        return parents[item]
        
    def union(self, parents, ranks, item1, item2):
        parent1 = self.find(parents, item1)
        parent2 = self.find(parents, item2)
        
        if ranks[parent1] > ranks[parent2]:
            parents[parent2] = parent1
        if ranks[parent1] < ranks[parent2]:
            parents[parent1] = parent2
        else:
            ranks[parent1] += 1
            parents[parent2] = parent1
            
print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
        
        
            