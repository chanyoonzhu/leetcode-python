class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        
        table = collections.defaultdict(tuple)
        res = []
        
        for n in nums1:
            if n not in table:
                table[n] = (1,1)
            else:
                num1Sum, num2Diff = table[n]
                table[n] = (num1Sum+1, num2Diff+1)
        
        for n in nums2:
            if n in table:
                num1Sum, num2Diff = table[n]
                table[n] = (num1Sum, num2Diff-1)
                
        for item in table.items():
            for _ in range(item[1][0]-max(0,item[1][1])): # df: when item[1][1] is negative, use 0 instead!
                res.append(item[0])
                
        return res