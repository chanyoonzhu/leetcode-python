class Solution:
    """
    - two pointers
    - O(mn), O(n)
    """
    def shortestWay(self, source: str, target: str) -> int:
        
        source_set = set()
        for c in source:
            source_set.add(c)
        
        result = 0
        i, j, n, m = 0, 0, len(source), len(target)
        while j < m:
            if target[j] not in source_set:
                return -1
            if i == n:
                result += 1
                i = 0
            while i < n:
                if source[i] == target[j]:
                    j += 1
                    i += 1
                    break
                i += 1
                  
        return result + 1
    
    """
    - two pointers: optimized using modulo
    - O(mn), O(n)
    """
    def shortestWay(self, source: str, target: str) -> int:
        
        source_set = set()
        for c in source:
            source_set.add(c)
        
        i, j, n, m = 0, 0, len(source), len(target)
        while j < m:
            if target[j] not in source_set:
                return -1
            while source[i % n] != target[j]:
                i += 1
            i += 1
            j += 1
                  
        return math.ceil(i / n)
    
    """
    - hashmap + binary search
    - O(mlogn), O(n)
    """
    def shortestWay(self, source: str, target: str) -> int:
        
        source_index = collections.defaultdict(list)
        for i, c in enumerate(source):
            source_index[c].append(i)
        
        i, j, n, m = 0, 0, len(source), len(target)
        result = 0
        for c in target:
            if c not in source_index:
                return -1
            indexes = source_index[c]
            curr = bisect.bisect_left(indexes, i)
            if curr == len(indexes):
                result += 1
                i = indexes[0] + 1
            else:
                i = indexes[curr] + 1
                  
        return result + 1