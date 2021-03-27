class Solution:

    """
    - sliding window with sorting
    - caveat: subsequence is different from substring, subsequence doesn't need to have consecutive elements
    - O(nlogn), O(n)
    """
    def numSubseq(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        nums.sort()
        mod = 10 ** 9 + 7
        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result += 2 ** (right - left) % mod
                left += 1
            else:
                right -= 1
        return result % mod