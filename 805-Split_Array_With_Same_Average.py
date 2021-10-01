"""
- dynamic programming - knapsack
- O(n^2*sum), O(n*sum)
"""
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        N = len(nums)
        M = int(N / 2)
        sum_ = sum(nums)   

        """
        - early pruning
        """
        # can_split = False 
        # for i in range(1, M + 1):
        #     if sum_ * i % N == 0:
        #         can_split = True
        #         break 
        # if not can_split:
        #     return False 
        
        # knapsack
        sums = [set() for _ in range(M + 1)]
        sums[0].add(0)  
        for num in nums:
            for i in range(M, 0, -1):
                for t in sums[i - 1]:
                    sums[i].add(t + num)

        # search
        """
        If the array of size n can be splitted into group A and B with same mean, assuming A is the smaller group, then
        totalSum/n = Asum/k = Bsum/(n-k), where k = A.size() and 1 <= k <= n/2;
        Asum = totalSum*k/n, which is an integer. So we have totalSum*k%n == 0;
        """
        for i in range(1, M + 1):
            if sum_ * i % N == 0 and int(sum_ * i / N) in sums[i]: # test if sum_ * i / N == any subsequence sum in sums[i]
                return True
        return False