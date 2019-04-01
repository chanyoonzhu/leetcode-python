class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        """
        - O(n), O(n)
        - two pass with one array
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
        - two pass with a constant
        """