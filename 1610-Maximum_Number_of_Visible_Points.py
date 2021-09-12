"""
- sliding window with sorting (using radian)
- O(nlogn)
"""
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        arr, extra = [], 0
        xx, yy = location
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            arr.append(math.atan2(y - yy, x - xx)) # append radians (0 degree - 0, 90 - 1.57, 180 - pi, 270 - -1.57, 360 - 2 * pi)
        
        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr] # create a "circular array" so we can use min(angle, 360 - angle)
        angle = math.pi * angle / 180 # convert to radian
        
        # sliding window
        l = result = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            result = max(result, r - l + 1)
            
        return result + extra
        