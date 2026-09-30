"""
- dynamic programming
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(fuel, i):
            station_pos, station_fuel = (stations[i]) if i < len(stations) else (target, 0)
            remain_fuel = fuel - (station_pos - (stations[i-1][0] if i > 0 else 0))
            if remain_fuel >= target - station_pos:
                return 0
            if remain_fuel < 0: # cannot reach
                return float("inf") 
            return min(dp(remain_fuel + station_fuel, i + 1) + 1, dp(remain_fuel, i + 1))
        
        res = dp(startFuel, 0)
        return res if res < float("inf") else -1

"""
- greedy with heap
- O(nlogn), O(n)
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        stations.append([target, 0])
        heap = []
        cur_fuel, cur_pos = startFuel, 0
        res = 0
        for pos, fuel in stations:
            cur_fuel -= (pos - cur_pos)
            cur_pos = pos
            while heap and cur_fuel < 0: # greedily pick the station with most gas
                cur_fuel -= heapq.heappop(heap)
                res += 1
            if cur_fuel < 0:
                return -1
            heapq.heappush(heap, -fuel)
        return res