"""
- greedy
- intuition: https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/508543/APPLES-and-BANANAS-solution-(with-picture)
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = [] # groups of chars, each group abides by the rule
        chars = sorted(zip([a, b, c], ['a', 'b', 'c']), reverse=True)
        max_count, max_c = chars[0]
        mid_count, mid_c = chars[1]
        min_count, min_c = chars[2]
        
        res = [max_c + max_c] * (max_count // 2) + [max_c] * (max_count % 2) # put all high freq chars, two per group
        
        i = 0
		# Now delimit existing groups with mid/low freq chars
        max_i = i # index of the last high freq chars group that got delimited with at least one mid/low freq chars, need to discard groups not delimited since once they got squashed together there'll be 3 or more.
        # put all mid/low freq chars, one at a time in a round robin fashion
        for _ in range(mid_count): 
            if i == len(res):
                i = 0
            res[i] += mid_c
            i += 1
            max_i = max(i, max_i)
        for _ in range(min_count):
            if i == len(res):
                i = 0
            res[i] += min_c
            i += 1
            max_i = max(i, max_i)
        
        return ''.join(res[:max_i+1])

"""
- greedy
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = [] # groups of chars, each group abides by the rule

        # sort characters by counts
        chars = sorted(zip([a, b, c], ['a', 'b', 'c']), reverse=True)
        max_count, max_c = chars[0]
        mid_count, mid_c = chars[1]
        min_count, min_c = ch
        ars[2]
		
        # Stage 1: consume all mid_c
        # consume one char with max count and one with mid count per group, until all mid chars are all used - now only has max and min chars left
        while mid_count:
            res.append(max_c + mid_c)
            max_count -= 1
            mid_count -= 1
			
        # Stage 2: consume all max_c
        # consume remaining max chars in existing group by adding one max char per group
        i = 0
        while max_count and i < len(res):
            res[i] = max_c + res[i] # "ca" -> "cca"
            i += 1
            max_count -= 1
        # consume remaining max chars using min chars as delimiter (greedily consume 2 max_c and 1 min_c, since max_c cannot be consumed elsewhere, but min_c can be all consumed in groups created in stage 1 since stage1 created mid_count number of groups and min_count <= mid_count)
        while max_count and min_count:
            res.append(max_c * min(2, max_count) + min_c) # easy to miss: edge case - max_count == 1
            max_count -= min(2, max_count)
            min_count -= 1
        if max_count: # easy to miss: can consume two more max_c at the end
            res.append(max_c * min(2, max_count))
		
        # Stage 3: consume all min_c
		# consume one per group for groups created at stage 1
        i = 0
        while min_count:
            res[i] = res[i] + min_c
            min_count -= 1
            i += 1
        return ''.join(res)