class Solution(object):
    """
    Questions to ask: 
    Q: Children with a higher rating get more candies than their neighbors. What about the same rating? 
    A: can be higher or lower. eg: ratings: [6,5,4,4,3,2] candies needed: [3,2,1,3,2,1]
    """
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        """
        - O(n), O(n)
        - two pass with one array: first pass only satisfy condition with left neighbor, second pass satisfy condition with right neighbor 
        - and pick max of current and first pass
        """
        
        n = len(ratings)
        
        candies = [1] * n
        
        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1
                
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        
        return sum(candies)
    
        """
        - O(n), O(1)
        - only the local increasing and decreasing sequences determine the candies needed, a rating equal to the previous rating resets the candy needed to 1. What's happening in the next increasing/decreasing period won't affect the previous one.
        """
            
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # up - number of continuous increasing rating before current child, also the number of candies needed for the left neighbor
        # down - number of continuous decreasing ratings before current child, also the number of candies needed for the child at the head of decreasing sequence, also the number of candies needed to compensate for all previous children that form continuous decreasing sequence when a member adds to the decreasing sequence
        # peak - number of candies needed for the child at local rating peak
        peak = up = down = 0
        total = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]: # rating increases
                up += 1
                peak = up
                down = 0
                total += 1 + up # one plus the number of candies needed for the left neighbor
            elif ratings[i] == ratings[i-1]: # rating flats
                peak = up = down = 0
                total += 1 # only need one candie
            else: # rating decreases
                up = 0
                down += 1 # increase current hill-down height
                compensation = down + (-1 if peak >= down else 0) # don't need to compensate the child at the head of decreasing sequence if he already has more
                total += 1 + compensation # one plus the number of candies needed for compensating all previous children that form continuous decreasing sequence
        return total
        