"""
- hashmap with bitmask
- key: n can be much greater than r, how can this be optimized?
- O(r), O(r)
"""
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(int) 
        res = 0
		
        for row, col in reservedSeats:
            seats[row] = seats[row] | (1 << (col-1))

        for reserved in seats.values():
            groups = 0
            groups += (reserved & int('0111100000', 2)) == 0
            groups += (reserved & int('0000011110', 2)) == 0
            if not groups: groups += (reserved & int('0001111000', 2)) == 0
            res += groups

        return res + 2 * (n - len(seats))