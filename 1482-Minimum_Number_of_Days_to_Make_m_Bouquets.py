class Solution:

    """
    - binary search + greedy
    - O(nlogK), O(1) - K is the largest bloom day
    """
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        days = max(bloomDay)
        
        def binary_search(l, r):
            if l == r:
                return l
            mid = l + (r - l) // 2
            if can_make(mid):
                return binary_search(l, mid)
            else:
                return binary_search(mid + 1, r)
        
        def can_make(target_day):
            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day > target_day:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    if bouquets == m:
                        return True
                    flowers = (flowers + 1) % k               
            return False
        
        """ my initial solution for can_make function
        def can_make(target_day):
            is_consecutive = True
            bouquets = 0
            current_bloom = 0
            for day in bloomDay:
                if day <= target_day:
                    if is_consecutive:
                        current_bloom += 1
                    else:
                        current_bloom = 1
                        is_consecutive = True
                    if current_bloom == k:
                        bouquets += 1
                        if bouquets >= m:
                            return True
                        current_bloom = 0
                else:
                    is_consecutive = False
            return False
        """ 

        if m * k > len(bloomDay):
            return -1
        return binary_search(1, days)
    
