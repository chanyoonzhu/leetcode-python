class Solution:

    """
    - sort then swap
    - O(nlogn), O(1)
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 1
        while i < len(nums) - 1:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        return nums

    """
    - one pass swap
    - O(n), O(1)
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isNextLargerOrEqual = True
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if isNextLargerOrEqual and diff < 0 or not isNextLargerOrEqual and diff > 0:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            isNextLargerOrEqual = not isNextLargerOrEqual
        return nums