class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        - Questions: buy first, then sell?
        - negative numbers? empty array? numbers getting smaller and smaller - Don't buy?
        
        - Brute Force
        - O(n^2), O(1)
        - time limit exceeded
        
        maxProfit = 0
        
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
                
        return maxProfit
        """
        
        """
        - One pass 1: buy index increase until value smaller than sell, 

                
        maxProfit = 0
        buy = sell = 0
        
        while sell < len(prices):
            if prices[buy] <= prices[sell]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
                sell += 1
            else:
                buy = sell
            
        return maxProfit
        """

        """
        - One pass 2:
        """

        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        
        return maxProfit