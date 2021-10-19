"""
- set
- intuition: only start to traverse sequence when n is the lowest number in sequence
- O(n), O(n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for n in nums:
            cur_seqlen = 1
            next_n = n + 1
            if n - 1 not in nums_set:
                while next_n in nums_set:
                    cur_seqlen += 1
                    next_n += 1
                result = max(result, cur_seqlen)
        return result

"""
- union find
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        parents = {n: n for n in nums}
        
        def find(n):
            if parents[n] != n:
                parents[n] = find(parents[n])
            return parents[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                parents[p1] = p2
    
        allNums = set(nums)
        
        for n in nums:
            parents[n] = n
            if n - 1 in allNums:
                union(n, n - 1)
            if n + 1 in allNums:
                union(n + 1, n)
        
        counter = collections.Counter()
        for c, _ in parents.items():
            counter[find(c)] += 1
        return max(counter.values())       