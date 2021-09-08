"""
- Sort and compare
- O(1), O(1)
"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def distSquare(a, b):
            x1, y1 = a
            x2, y2 = b
            return (x2 - x1) ** 2 + (y2 - y1) ** 2
    
        dists = [distSquare(x, y) for x, y in [(p1, p2), (p2, p3), (p3, p4), (p4, p1), (p1, p3), (p2, p4)]]
        dists.sort()
        if dists[0] == dists[1] == dists[2] == dists[3] != 0 and dists[4] == dists[5]:
            return True
        return False