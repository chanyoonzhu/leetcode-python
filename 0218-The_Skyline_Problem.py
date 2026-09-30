import heapq
class Solution:
    def getSkyline(self, buildings):

        """
        - sweep lines: my solution
        - O(nlogn), O(n)
        - time limit exceeded
        """
        def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
                
        lines = []
        for start, end, height in buildings:
            lines.append((start, -1, -height))
            lines.append((end, 1, height))
        lines.sort()
            
        active = []
        result = []
        for x, _type, height in lines:
            if _type == -1:
                height = -height
            if _type == -1:
                if height > -active[0]:
                    result.append((x, height))
                heapq.heappush(active, -height)
            else:
                temp = []
                while active and -active[0] >= height:
                    temp.append(heapq.heappop(active))
                
                if len(temp) == 1:
                    result.append((x, -active[0] if active else 0))
                    
                    
                for height_neg in temp[:-1]:
                    heapq.heappush(active, height_neg)
        
        return result

        """
        - Better solution
        - O(nlogn), O(n)
        """
        events = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, None) for _, R, _ in buildings])
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: # remove inactive buildings
                heapq.heappop(hp)
            if negH:  # for left side
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: # get rid of duplicates
                res += [x, -hp[0][0]],
        return res[1:]

    """
    - my solution: line sweeping with heap and set (tracking which buildings are in range)
    set is not needed actually, can use end value to filter elements popped out from the heap
    """
    def getSkyline_heap_and_set(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        pq = []
        curr = set()
        prev = 0
        res = []
        min_x = min([start for start, _, _ in buildings]) - 1
        max_x = max([end for _, end, _ in buildings]) + 1
        lines = sorted(([(start, end, height) for start, end, height in buildings] + [(end, start, -height) for start, end, height in buildings] + [(min_x, max_x, 0), (max_x, min_x, 0)]), key = lambda x: (x[0], -x[2]))
        for x1, x2, height in lines:
            if x1 < x2:
                curr.add((-height, x1, x2))
                heapq.heappush(pq, (-height, x1, x2))
                height_neg, start, end = heapq.heappop(pq)
                while (height_neg, start, end) not in curr:
                    height_neg, start, end = heapq.heappop(pq)
                heapq.heappush(pq, (height_neg, start, end))
                if -height_neg > prev:
                    prev = -height_neg
                    res.append((x1, height))                    
            else:
                curr.discard((height, x2, x1))
                height_neg, start, end = heapq.heappop(pq)
                while pq and (height_neg, start, end) not in curr:
                    height_neg, start, end = heapq.heappop(pq)
                heapq.heappush(pq, (height_neg, start, end))
                if -height_neg < -height and x1 != res[-1][0]:
                    res.append((x1, -height_neg))
                    prev = -height_neg
        return res
                
s = Solution()
s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
s.getSkyline([[1,2,1],[1,2,2],[1,2,3]])
s.getSkyline([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]])
                
            
        
                
                
        
        
                
                
            