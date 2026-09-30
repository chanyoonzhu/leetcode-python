"""
- greedy
- O(n), O(1)
- intuition: imagine gas in tank can be negative, find the index at which tank has the minimum value, 
    the starting point must be the next index (so that we can start to gain as much gas as possible to cover the loss)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        min_tank_idx = 0
        min_tank = float("inf")
        
        total = 0
        for i in range(N):
            total += gas[i] - cost[i]
            if total < min_tank:
                min_tank = total
                min_tank_idx = i
        
        if total < 0:
            return -1
        
        return (min_tank_idx + 1) % N

"""
- greedy
- O(n), O(1)
- intuition: https://github.com/wisdompeak/LeetCode/tree/master/Greedy/134.Gas-Station
    1. If the total number of gas is bigger than the total number of cost. There must be a solution.
    2. If car starts at A and can not reach B. Any station between A and B
        can not reach B.(B is the first station that A can not reach.)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        total = 0
        for i in range(N):
            total += gas[i] - cost[i]
        if total < 0:
            return -1
        
        tank = 0
        start = 0
        for i in range(N):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start
        