class Solution:

    """
    - dynamic programming (bottom-up): dp[i] a list of the length of the last step to reach position i in the river
    - O(n^3), O(n^2)
    - time limit exceeded
    """
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if n <= 2:
            return stones[1] == 1
        dp = [list() for _ in range(n)]
        dp[0] = []
        dp[1] = [1]
        for i in range(2, n):
            for j in range(i):
                for prev_steps in dp[j]:
                    steps = stones[i] - stones[j]
                    if steps >= prev_steps - 1 and steps <= prev_steps + 1:
                        dp[i].append(steps)
                
        if dp[-1]:
            return True
        return False
    
    """
    - dynamic programming (bottom-up): dp[i] a list of the length of the last step to reach position i in the river
    - optimized using bisect
    - O(n^2logn), O(n^2)
    - buggy (one case failed, needs debugging)
    """
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [list() for _ in range(n)]
        dp[0], dp[1] = [], [1]
        for i in range(2, n):
            for j in range(i):
                steps = stones[i] - stones[j]
                idx = bisect.bisect_left(dp[j], steps)
                if idx < len(dp[j]):
                    prev_steps = dp[j][idx]
                    if prev_steps == steps or prev_steps - 1  == steps:
                        bisect.insort_left(dp[i], steps)
                        break
                if idx > 0:
                    prev_steps = dp[j][idx - 1]
                    if prev_steps == steps or prev_steps + 1  == steps:
                        bisect.insort_left(dp[i], steps)
                
        if dp[-1]:
            return True
        return False
    
    """
    - dynamic programming (bottom-up) with hashmap: key - stone position value - set of steps to arrive at this position
    - optimized using bisect
    - O(n^2logn), O(n^2)
    - buggy (one case failed, needs debugging)
    """
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        position_to_steps = dict()
        for position in stones:
            position_to_steps[position] = set()
        position_to_steps[0].add(0)
        for i in range(0, n):
            for step in position_to_steps[stones[i]]:
                for next_step in range(max(step - 1, 1), step + 2):
                    next_position = stones[i] + next_step
                    if next_position in position_to_steps:
                        position_to_steps[next_position].add(next_step)
                
        return len(position_to_steps[stones[n - 1]]) > 0