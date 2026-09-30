class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import heapq
        
        table = collections.defaultdict(int)
        res = []
        
        for word in words:
            table[word] += 1
            
        heap = [(-item[1], item[0]) for item in table.items()]
        heapq.heapify(heap)
        
        while heap and k:
            negCount, word = heapq.heappop(heap)
            res.append(word)
            k -= 1
        
        return res