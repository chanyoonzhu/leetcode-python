class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        max_capacity = sum(weights)
        min_capacity = max(weights)
        
        def binary_search(l, r):
            if l == r:
                return l
            mid = l + (r - l) // 2
            if can_ship(mid):
                return binary_search(l, mid)
            else:
                return binary_search(mid + 1, r)
        
        def can_ship(capacity):
            days_taken = 0
            load = 0
            for weight in weights:
                load += weight
                if load > capacity:
                    days_taken += 1
                    load = weight
            if load > 0: days_taken += 1
            return days_taken <= D
        
        """ other solutions:
        def can_ship(capacity):
            days_taken = 0
            load = 0
            for weight in weights:
                if (load + weight > capacity):
                    days_taken += 1
                    load = 0
                load += weight
            if load: days_taken += 1
            return days_taken <= D
        """
        
        return binary_search(min_capacity, max_capacity)