class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def canFlood(r, c, color):
            return (r >= 0 and r < len(image) 
                    and c >= 0 and c < len(image[0]) 
                    and image[r][c] == color)
        
        def floodNeighbors(sr, sc, oldColor, newColor):
            image[sr][sc] = newColor
            if canFlood(sr - 1, sc, oldColor):
                image[sr-1][sc] = newColor
                floodNeighbors(sr-1, sc, oldColor, newColor)
            if canFlood(sr + 1, sc, oldColor):
                image[sr+1][sc] = newColor
                floodNeighbors(sr+1, sc, oldColor, newColor)
            if canFlood(sr, sc - 1, oldColor):
                image[sr][sc-1] = newColor
                floodNeighbors(sr, sc-1, oldColor, newColor)
            if canFlood(sr, sc + 1, oldColor):
                image[sr][sc+1] = newColor
                floodNeighbors(sr, sc+1, oldColor, newColor)
        
        if image[sr][sc] != newColor:
            floodNeighbors(sr, sc, image[sr][sc], newColor)
            
        return image