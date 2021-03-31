class Solution:

    """
    - binary search + greedy
    - O(nlogK) K - pile total, O(1)
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = max(piles)
        
        def binary_search(l, r):
            if l == r:
                return l
            mid = l + (r - l) // 2
            if can_finish(mid):
                return binary_search(l, mid)
            else:
                return binary_search(mid + 1, r)
        
        def can_finish(speed):
            time = 0
            for n in piles:
                time += ceil(n / speed)
                if time > h:
                    return False
            return True
    
        return binary_search(1, total)