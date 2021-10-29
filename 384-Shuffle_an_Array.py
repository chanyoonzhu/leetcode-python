"""
- math
- O(n), O(n)
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        return self.nums
        

    def shuffle(self) -> List[int]:
        res = self.nums[:]
        N = len(res)
        for i in range(N - 1):
            j = random.randint(i, N - 1) # caveat: i, not i - 1 because a number can have the chance to stay
            res[i], res[j] = res[j], res[i]
        return res