"""
- greedy
- O(n) - 26 * n, O(n)
- intuition: sort by end index, try inserting substrings with smaller index first
"""
class Solution:

    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        ranges = dict()
        for i, c in enumerate(s):
            if c not in ranges:
                ranges[c] = [i, i]
            ranges[c][0] = i
        
        """
        this chunk deals with cases like "abab", original ranges[a] is [0, 2], updated ranges[a] is [0, 3] because it has to cover the range of b too
        """
        for c in set(s):
            r, l = ranges[c]
            l_temp, r_temp = -1, -1
            while not (l_temp == l and r_temp == r):
                l_temp, r_temp = l, r
                r = max([ranges[c_temp][0] for c_temp in set(s[l:r+1])])
                l = min([ranges[c_temp][1] for c_temp in set(s[l:r+1])])
            ranges[c] = [r, l]
        
        result = []
        last_r = -1
        for r, l in sorted(ranges.values()):
            if l > last_r:
                result.append(s[l:r + 1])
                last_r = r
        return result