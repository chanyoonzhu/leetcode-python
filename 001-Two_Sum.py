class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        
        """
        - Questions:
            * Can same element be used twice?
            * duplicate numbers?
            * many solutions?
            * no solution?
        - Caveats:
            * same number can appear multiple times - dic has to store list
            * same idx cannot be used multiple times - if statement
        - Solution:
            * O(n), O(n)
            * hash-table one pass
        """
        
        dic = collections.defaultdict(list)
        
        for i, n in enumerate(nums):
            dic[n].append(i)
            if target-n in dic:
                for j in dic[target-n]:
                    if j != i:
                        return [j, i]