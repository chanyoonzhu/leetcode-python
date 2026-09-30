class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        """
        vec1x, vec2x, vec1y, vec2y = [rec1[0],rec1[2]], [rec2[0],rec2[2]], [rec1[1],rec1[3]], [rec2[1],rec2[3]]
        return (max(vec1x + vec2x) - min(vec1x + vec2x) < vec1x[1] - vec1x[0] + vec2x[1] - vec2x[0] and 
                max(vec1y + vec2y) - min(vec1y + vec2y) < vec1y[1] - vec1y[0] + vec2y[1] - vec2y[0])
        """
        
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]
        