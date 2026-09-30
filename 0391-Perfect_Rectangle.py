class Solution:
    """
    - sweep line (2D)
    - O(n*2logn), O(n)
    """
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        OPEN, CLOSE = 1, 0
        events = []
        min_x, max_x = float("inf"), float("-inf")
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            max_x = max(max_x, x2)
            events.append([y1, OPEN, x1, x2])
            events.append([y2, CLOSE, x1, x2])
        events.sort()
        
        def is_rectangle_in_subsection():
            prev_x2 = min_x
            for x1, x2 in active:
                if x1 != prev_x2:
                    return False
                prev_x2 = x2
            return prev_x2 == max_x
                
        active = []
        curr_y = float("inf")
        for y, _type, x1, x2 in events:
            if _type == OPEN:
                active.append((x1, x2))
                active.sort()
                # bisect.insort(active, (x1, x2))
            else:
                if y != curr_y and not is_rectangle_in_subsection(): # when y != curr_y, don't need to validate
                    return False
                active.remove((x1, x2))
                curr_y = y
        return True
    
    """
    - math: area match + no intersection
    - O(n^2), O(n)
    - time limit exceeded
    """
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        OPEN, CLOSE = 1, 0
        events = []
        min_x, min_y, max_x, max_y = float("inf"), float("inf"), float("-inf"), float("-inf")
        area_total = 0
        for x1, y1, x2, y2 in rectangles:
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            events.append([y1, OPEN, x1, x2])
            events.append([y2, CLOSE, x1, x2])
            area_total += (x2 - x1) * (y2 - y1)
        events.sort()
        if area_total != (max_x - min_x) * (max_y - min_y):
            return False
        
        for i in range(len(rectangles)):
            x1_i, y1_i, x2_i, y2_i = rectangles[i]
            for j in range(i + 1, len(rectangles)):
                x1_j, y1_j, x2_j, y2_j = rectangles[j]
                if not (x1_j >= x2_i or x2_j <= x1_i or y1_j >= y2_i or y2_j <= y1_i):
                    return False
        return True

    """
    - math: area match + four max corners only show up once and other corners number of times showing up is even
    - O(n), O(n)
    """
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x, min_y, max_x, max_y = float("inf"), float("inf"), float("-inf"), float("-inf")
        corner_count = defaultdict(int)
        area = 0
        for x1, y1, x2, y2 in rectangles:
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            corner_count[(x1, y1)] += 1
            corner_count[(x2, y2)] += 1
            corner_count[(x1, y2)] += 1
            corner_count[(x2, y1)] += 1
            area += (y2 - y1) * (x2 - x1)
        if area != (max_y - min_y) * (max_x - min_x):
            return False
            
        for corner, count in corner_count.items():
            if corner == (min_x, min_y) or corner == (min_x, max_y) or corner == (max_x, max_y) or corner == (max_x, min_y):
                if count != 1:
                    return False
            elif count % 2 != 0:
                return False
        return True
                
        