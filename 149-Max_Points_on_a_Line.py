"""
- hashmap
- use a, b, c in the line function as map key (cannot use a/b because float is not accurate), a distinct a, b, c represents a unique line in the plane
https://leetcode.com/problems/max-points-on-a-line/discuss/224773/Python-Easy-and-Concise-with-Detailed-Explanation-Algebra
- O(n^2 * O(gcd)), O(n^2)
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        if n < 3:
            return n
        
        lines_to_points = collections.defaultdict(set)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                a, b, c = x2 - x1, y2 - y1, x2 * y1 - x1 * y2
                
                if not a: # easy to miss: vertical
                    b, c = 1, x1
                elif not b: # easy to miss: horizontal
                    a, c = 1, y1
                else:
                    if a < 0: # easy to miss: always make a positive
                        a, b, c = -a, -b, -c
                    gcd = math.gcd(a, b)
                    a, b, c = a / gcd, b / gcd, c / gcd
                lines_to_points[(a, b, c)].add((x1, y1))
                lines_to_points[(a, b, c)].add((x2, y2))
            
        result = 0
        for p_set in lines_to_points.values():
            result = max(result, len(p_set))
        
        return result

        """ can use math.gcd
        def gcd(n1, n2):
            if n1 < 0:
                n1 = -n1
            if n2 < 0:
                n2 = -n2
            while n1 != n2:
                if n1 > n2:
                    n1 -= n2
                else:
                    n2 -= n1
            return n1
        """
            
        