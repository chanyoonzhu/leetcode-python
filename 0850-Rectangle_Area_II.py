class Solution:
    """
    - sweep line (2D): sweep ys, count area between ys (using area() function) and add to anwer
    - O(n^2logn), O(n)
    """
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()
        
        def area():
            covered = 0
            curr = float("-inf")
            for x1, x2 in active:
                curr = max(curr, x1)
                covered += max(0, x2 - curr)
                curr = max(curr, x2)
            return covered
        
        active = []
        ans = 0
        curr_y = events[0][0]
        for y, _type, x1, x2 in events:
            ans += area() * (y - curr_y)
            if _type == OPEN:
                active.append((x1, x2))
                active.sort()
                # or replacing previous two lines with bisect.insort(active, (x1, x2)) to lower time comlexity to (n^2) 
                # since insort complexity is O(n) - complexity of python string insertion
            else:
                active.remove((x1, x2))
            
            curr_y = y
        
        return ans % (10**9 + 7)
    
    """
    - segment tree: todo
    """