class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        
        table = {}
        res = []

        for n in nums1:
            if n not in table:
                table[n] = -1
                
        for n in nums2:
            if n in table and table[n] != 0:
                table[n] += 1
                
        res = [item[0] for item in table.items() if item[1] == 0]
        
        return res