"""
- greedy with sort
- O(nlogn), O(logn)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h, n = 0, len(citations)
        while h < n:
            if citations[h] <= h : # citations[:h+1] all larger than citation[h], if citations[h] > h, there are h citations that have more than h citations, then increase h + 1 and test again
                break
            h += 1
        return h

"""
- count sort
- intuition: count arrary with idx - min(citation number, n), value - number of papers with citation == idx 
    - we take the min(citation number, n) because h is bound by n and taking the min could result in using less memory
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0 for _ in range(n + 1)]
        
        for num in citations:
            if num >= n:
                buckets[n] += 1
            else:
                buckets[num] += 1
                
        count = 0
        
        for i in reversed(range(len(buckets))):
            count += buckets[i]
            
            if count >= i:
                return i
                
        return 0