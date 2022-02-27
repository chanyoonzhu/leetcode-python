"""
- math
- intuition: there are only two patterns each row(or col) could have: the pattern of the first row, or the reversed-pattern of the first row
- proof: 
    1. supposed a group of flips can bring all the elements to 0, for each cell, the total number of flips will stay static no matter how we change the sequences of the flips, 
    so the end status of each cell should stay the same disregard the sequence of flips
    2. lets do all the row flips first and then the col flips, for col flips to be able to get all 0s, each col needs to be either all 0 or all 1
    3. for each col to be either all 0 or all 1, each row must be of only two patterns that are exclusive of each other (anti-pattern)
"""
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        pattern = grid[0]
        inverted_pattern = [1 - x for x in pattern]
        
        for i in range(1, len(grid)):
            if grid[i] != pattern and grid[i] != inverted_pattern:
                return False
        return True