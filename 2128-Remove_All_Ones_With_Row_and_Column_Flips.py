"""
- math
- https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1671908/Python-3-or-Math-or-Explanation
"""
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        pattern = grid[0]
        inverted_pattern = [1 - x for x in pattern]
        
        for i in range(1, len(grid)):
            if grid[i] != pattern and grid[i] != inverted_pattern:
                return False
        return True