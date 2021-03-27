class Solution:

    """
    - sliding window
    - O(n), O(1)
    - algorithm:
        - starting from num[k], expanding to the side which has smaller value
        - calculate max_score as expansion goes on
        - update min as new min appears
    - similar: 1537
    """
    def maximumScore(self, nums: List[int], k: int) -> int:
        curr_min = nums[k]
        max_score = curr_min
        left = right = k
        while left > 0 or right < len(nums) - 1:
            if left > 0 and (right == len(nums) - 1 or nums[left - 1] > nums[right + 1]):
                left -= 1
                curr_min = min(curr_min, nums[left])
            else:
                right += 1
                curr_min = min(curr_min, nums[right])
            max_score = max(max_score, curr_min * (right - left + 1))
        return max_score