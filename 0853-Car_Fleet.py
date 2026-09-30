"""
- greedy
- O(nlogn), O(n)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrivals = []
        for pos, v in sorted(zip(position, speed))[::-1]: # greedily handles car at the largest pos
            arrival_time = (target - pos) / v
            if not arrivals or arrivals[-1] < arrival_time:
                arrivals.append(arrival_time) # append if a car takes longer time to arrive than current fleet
        return len(arrivals)