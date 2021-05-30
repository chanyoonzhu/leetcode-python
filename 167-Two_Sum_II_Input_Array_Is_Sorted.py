class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            sum_ = numbers[l] + numbers[r]
            if sum_ == target:
                return [l + 1, r + 1] # caveat: 1-indexed
            elif sum_ > target:
                r -= 1
            else:
                l += 1