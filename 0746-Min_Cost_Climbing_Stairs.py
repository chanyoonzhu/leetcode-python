class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        """
        dp:
        
        if len(cost) == 0:
        return 0
        
        cost.append(0)
        dp = [0] * (len(cost))
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]           
        return dp[-1]
        """

        dp = [0]*(len(cost))
        dp[0], dp[1]=cost[0], cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])
        
        return min(dp[-2], dp[-1])