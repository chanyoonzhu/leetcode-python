"""
- dfs with hashmap
- O(n), O(n)
"""
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        self.result = 0
        value_map = dict()
        for num in nums:
            identifier = num / 10 # 10 * depth + pos, which is unique
            value_map[identifier] = num % 10 # value
            
        def dfs(node_id, total):
            if node_id not in value_map:
                return
            total += value_map[node_id]
            d, p = divmod(node_id, 10)
            
            left_id = (d + 1) * 10 + 2 * p - 1
            right_id = left_id + 1
            
            if left_id not in value_map and right_id not in value_map:
                self.result += total
            else:
                dfs(left_id, total)
                dfs(right_id, total)
                
        dfs(nums[0] / 10, 0)
        return self.result
            
            
            
        