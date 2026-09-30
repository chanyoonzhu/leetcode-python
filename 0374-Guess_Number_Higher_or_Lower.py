# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def binary_search(small, large):
            while small < large:
                mid = small + (large - small) // 2
                curr_result = guess(mid)
                if curr_result == 0:
                    return mid
                elif curr_result == -1:
                    large = mid - 1
                else:
                    small = mid + 1
            return small
        
        return binary_search(1, n)