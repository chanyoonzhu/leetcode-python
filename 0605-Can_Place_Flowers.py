"""
- Array
- O(n)
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        planted = 0
        N = len(flowerbed)
        while i < N:
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == N-1 or flowerbed[i+1] == 0: # easy to miss: i == N-1
                    planted += 1
                    i += 2
                    if planted >= n:
                        return True
                else:
                    i += 1
        return planted >= n # easy to miss: cannot just return True for edge case: planted = n = 0

"""
- Array
- with cleaner logic
- O(n)
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):            
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0: return True
        
        return False