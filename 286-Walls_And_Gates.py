class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q = [(i, j, 0)]
                    visited = [[0] * len(rooms[0]) for _ in rooms]
                    visited[i][j] = 1
                    while q:
                        x, y, dist = q.pop(0)
                        if self.updateDistance(rooms, visited, x-1, y, dist+1): q.append((x-1, y, dist+1))
                        if self.updateDistance(rooms, visited, x+1, y, dist+1): q.append((x+1, y, dist+1))
                        if self.updateDistance(rooms, visited, x, y-1, dist+1): q.append((x, y-1, dist+1))
                        if self.updateDistance(rooms, visited, x, y+1, dist+1): q.append((x, y+1, dist+1))
                        
    
    def updateDistance(self, rooms, visited, i, j, dist):
        if i >= 0 and i < len(rooms) and j >= 0 and j < len(rooms[0]):
            if not visited[i][j] and rooms[i][j] != -1 and rooms[i][j] != 0:
                visited[i][j] = 1
                rooms[i][j] = min(rooms[i][j], dist)
                return True
            visited[i][j] = 1
        return False
            
        