"""
- backtracking
- O(n*2^n), O(n)
"""
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        result = float("inf")
        group_size = len(nums) // k
        
        def backtrack(i, imcomp): 
            nonlocal result 
            nonlocal group_size
            if imcomp + len(nums) - i > result: return  # current run can't get smaller incompability
            if i == len(nums): 
                result = imcomp
            else: 
                for group_i in range(k): 
                    if len(groups[group_i]) < group_size and (not groups[group_i] or groups[group_i][-1] != nums[i]) and (group_i == 0 or groups[group_i - 1] != groups[group_i]): # current group has enough space for an extra element, nums[i] hasn't been added to this group yet, and it is different from the previous group
                        groups[group_i].append(nums[i])
                        if len(groups[group_i]) == 1: 
                            backtrack(i + 1, imcomp)
                        else: 
                            backtrack(i + 1, imcomp + groups[group_i][-1] - groups[group_i][-2])
                        groups[group_i].pop()
        
        groups = [[] for _ in range(k)]
        backtrack(0, 0)
        return result if result < float("inf") else -1

"""
- todo: bit-masking
"""
        
        