"""
- sort + binary search
- O(nlogn)
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        info = sorted(zip(difficulty, profit), key=lambda x: x[0])
        largest_profit = [info[0][1]]
        difficulties = [d for d, _ in info]
        for i in range(1, len(info)):
            largest_profit.append(max(largest_profit[-1], info[i][1]))
            
        profits = 0
        for w in worker: # can also sort worker and use pointer
            idx = bisect.bisect_right(difficulties, w) - 1
            if idx >= 0:
                profits += largest_profit[idx]
        return profits