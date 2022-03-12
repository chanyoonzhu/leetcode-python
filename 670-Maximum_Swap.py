"""
- intuition: At each digit, if there is a larger digit that occurs later, we want the swap it with the largest such digit that occurs the latest.
- O(n), O(n)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))
        n_to_idx = {x: i for i, x in enumerate(digits)} # idx of last n
        for i, x in enumerate(digits):
            for d in range(9, x, -1): # find the largest
                if n_to_idx.get(d, -1) > i: # need to come after x
                    digits[i], digits[n_to_idx[d]] = digits[n_to_idx[d]], digits[i]
                    return int("".join(map(str, digits)))
        return num

"""
- greedy
- similar: 121-Best Time to Buy and Sell Stock (reversed)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        low_i = swap_l = len(nums)
        high_i = swap_r = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[high_i]:
                low_i = i
                swap_l, swap_r = low_i, high_i # greedily update with the smallest swap_l
            if nums[i] > nums[high_i]:
                high_i = i # update high seen so far
        if swap_l < swap_r:
            nums[swap_l], nums[swap_r]  = nums[swap_r], nums[swap_l]
        return int(''.join(nums))