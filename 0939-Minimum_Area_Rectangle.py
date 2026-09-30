class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        minArea = float('inf')
        pointsSet = set([tuple(p) for p in points])
        size = len(points)
        
        for i in range(size):
            for j in range(i+1, size):
                if (points[i][0] != points[j][0] and points[i][1] != points[j][1]
                    and (points[i][0], points[j][1]) in pointsSet and (points[j][0], points[i][1]) in pointsSet): # check if two points form the diagnal of a rectangle
                    minArea = min(minArea, abs(points[i][1] - points[j][1]) * abs(points[i][0] - points[j][0]))
                    
        return minArea if minArea != float('inf') else 0