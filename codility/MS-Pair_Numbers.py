"""
 Given an array N, return true if it is possible we can pair all the numbers in the array with equal values. E.g N = [1, 2, 2, 1] -> true as we can pair (N[0], N[3]) and (N[1], N[2]). N = [7, 7, 7] would return false.
"""
import collections

class Solution:
    def pairNumbers(self, nums: list) -> bool:
        counts = collections.Counter(nums)
        for n, count in counts.items():
            if count % 2 == 1:
                return False
        return True

s = Solution()
print(s.pairNumbers([1, 2, 2, 1]))
print(s.pairNumbers([2,2,2]))


