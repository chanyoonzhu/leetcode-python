class Solution:

    """
    - binary search + greedy
    - O(nlogK), O(1) - stack is taking space so is actually O(n)
    """
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        
        _min = min(sweetness)
        _max = sum(sweetness) // (K + 1)
        
        def binary_search(l, r):
            if l == r:
                return l
            mid = l + (r - l + 1) // 2
            if not can_divide(mid):
                return binary_search(l, mid - 1)
            else:
                return binary_search(mid, r)
            
        def can_divide(min_sweetness):
            curr_sweetness = 0
            pieces = 0
            for s in sweetness:
                curr_sweetness += s
                if curr_sweetness >= min_sweetness:
                    pieces += 1
                    curr_sweetness = 0    
            if pieces < K + 1:
                return False
            return True
        
        return binary_search(_min, _max)