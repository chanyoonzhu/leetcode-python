"""
- dynamic programming: dp[i] = minimum jump to reach lane i
- O(n), O(1)
"""
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:        
        dp = [1, 0, 1]
        
        for obs_lane in obstacles:
            if obs_lane:
                dp[obs_lane - 1] = float("inf") # need to jump to this lane from other lanes
            for lane in range(1, 4):
                if lane != obs_lane:
                    dp[lane - 1] = min(dp[lane - 1], dp[lane % 3] + 1, dp[(lane + 1) % 3] + 1)
        return min(dp)

"""
- greedy
- O(n), O(1)
"""
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        result = 0
        cur_lane = 2
        
        # greedily jump to the lane with the next stone at the farthest pos
        def find_next_farthest_stone_lane_and_pos(lanes, i):
            lanes = set(lanes)
            while i < len(obstacles):
                if obstacles[i] in lanes:
                    if len(lanes) == 1: return (min(lanes), i)
                    lanes.remove(obstacles[i])
                i += 1
            return (lanes.pop(), i)
        
        def find_available_lanes(cur_lane, stone_pos):
            return [lane for lane in range(1, 4) if lane != cur_lane and obstacles[stone_pos - 1] != lane]
        
        cur_lane, stone_pos = find_next_farthest_stone_lane_and_pos([2], 1)
        while stone_pos < len(obstacles):
            result += 1
            available_lanes = find_available_lanes(cur_lane, stone_pos)
            cur_lane, stone_pos = find_next_farthest_stone_lane_and_pos(available_lanes, stone_pos + 1)
        return result
                