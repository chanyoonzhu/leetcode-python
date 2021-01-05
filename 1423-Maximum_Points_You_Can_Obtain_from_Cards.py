class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)
        
        right, left = k - 1, 0
        largest = curr_sum = sum(cardPoints[:k])
        for i in range(k):
            left = n - 1 - i
            curr_sum = curr_sum - cardPoints[right] + cardPoints[left]
            largest = max(largest, curr_sum)
            right -= 1
        return largest
        
s = Solution()
s.maxScore([1,2,3,4,5,6,1], 3)