"""
- sliding window
- O(k), O(1)
"""
class Solution:
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = k, len(cardPoints)
        res = sum_ = sum(cardPoints[:k])
        for _ in range(k):
            l -= 1
            r -= 1
            sum_ = sum_ - cardPoints[l] + cardPoints[r]
            res = max(res, sum_)
        return res
        
s = Solution()
s.maxScore([1,2,3,4,5,6,1], 3)