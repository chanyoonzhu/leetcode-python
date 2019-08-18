class Solution:
    def getSkyline(self, buildings):
    
        import heapq

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
        - O(n^2logn), O(n)
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

s = Solution()
print(s.getSkyline([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]))
        
                
                
        
        
                
                
            