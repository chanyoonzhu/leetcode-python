"""
- binary search
- O(logn), O(1)
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        l = 0
        r = len(letters)
        while l < r:
            mid = l + (r - l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[l%len(letters)]