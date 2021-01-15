import heapq
class Solution:
    def getSkyline(self, buildings):

        """
        Use a heap to keep the max height ()
        Use a dictionary to keep current active nodes
        iterate through all edges sorted by their positions


        edges, heap, res = [], [], []
        active = {}
        # sorting key is important, sort by position then 'l' > 'r' then by height
        edges = sorted([(building[0], building[1], -building[2], 'l') for building in buildings] + [(building[1], building[0], -building[2], 'r') for building in buildings], key = lambda x: (x[0], x[3], x[2]))
        maxHeight = 0
        for pos, pos2, h, side in edges:
            h = -h
            if side == 'l':
                if h > maxHeight:
                    res.append([pos, h])
                    maxHeight = h
                if (pos, pos2) not in active or -h < active[(pos, pos2)]: # higher building replace building(s) in same position
                    heapq.heappush(heap, (-h, pos, pos2))
                    active[(pos, pos2)] = -h
            else:
                if (pos2, pos) in active and -h == active[(pos2, pos)]: # do nothing if it's not the highest building in that position
                    del active[(pos2, pos)]
                    hHeap = posHeap = pos2Heap = 0
                    found = False
                    while not found and heap: # pop until found the current active highest building
                        hHeap, posHeap, pos2Heap = heapq.heappop(heap)
                        if (posHeap, pos2Heap) in active and active[(posHeap, pos2Heap)] == hHeap:
                            found = True
                    if found:
                        if h > -hHeap and pos != pos2Heap:
                            res.append([pos, -hHeap])
                            maxHeight = -hHeap
                        heapq.heappush(heap, (hHeap, posHeap, pos2Heap))
                    elif res and [pos, -hHeap] != res[-1]:
                        maxHeight = 0
                        res.append([pos, 0])
        """   

        """
        - Better solution
        - O(nlogn), O(n)
        """
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
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
                
            
        
                
                
        
        
                
                
            