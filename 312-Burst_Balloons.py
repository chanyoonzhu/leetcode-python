class Solution:

    """
    - dp top-down: dp[i][j] = maximum coins bursting subset nums[i+1:j]
    - algorithm for each recursion: 
        1. iterate through ballons between i and j (exclusive of i and j)
        2. if there's no ballons between i and j (exclusive of i and j), return 0, else, in each iteration, assume all other ballons are already popped except current balloon and i and j
            calculate coins = nums[left] * nums[i] * nums[right] + self.dp(left, i) + self.dp(i , right)
        3. get the max coins among all iterations, memoize max and return   
    - O(n^3), O(n^2)
    - exceeds time limit 
    """
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        m_n_max = [[None] * len(nums) for _ in nums]
        return self.dp(nums, m_n_max, 0, len(nums) - 1)
        
    def dp(self, nums, m_n_max, left, right): # if calculating maximum coins bursting subset nums[i+1:j], 
        if m_n_max[left][right]:
            return m_n_max[left][right]
        
        if left + 1 == right: # nums[i+1:j] is empty
            m_n_max[left][right] = 0
            return 0
             
        maximum = float("-inf")
        for i in range(left + 1, right):
            curr = nums[left] * nums[i] * nums[right] + self.dp(nums, m_n_max, left, i) + self.dp(nums, m_n_max, i , right)
            maximum = max(maximum, curr)
        m_n_max[left][right] = maximum
        return maximum
    
    """
    - dp bottom-up: dp[i][j] = maximum coins bursting subset nums[i+1:j]  
    - O(n^3), O(n^2)
    """
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        m_n_max = [[0] * len(nums) for _ in nums]
    
        for right in range(1, len(nums)):
            for left in range(right - 1, -1, -1):
                maximum = 0
                for i in range(left + 1, right):
                    curr = nums[left] * nums[i] * nums[right] + m_n_max[left][i] + m_n_max[i][right]
                    maximum = max(maximum, curr)
                m_n_max[left][right] = maximum
        return m_n_max[0][len(nums) - 1]

    """
    - dp top-down: dp[i][j] = maximum coins bursting subset nums[i:j]
    - algorithm for each recursion: 
        1. iterate through ballons between i and j (inclusive of i and j)
        2. if there's no ballons between i and j (inclusive of i and j), return 0, else, in each iteration, assume all other ballons are already popped except current balloon
            calculate coins = nums[left - 1] * nums[i] * nums[right + 1] + self.dp(left, i - 1) + self.dp(i + 1 , right)
        3. get the max coins among all iterations, memoize max and return   
    - O(n^3), O(n^2)
    - exceeds time limit 
    """
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        m_n_max = [[None] * len(nums) for _ in nums]
        return self.dp(nums, m_n_max, 1, len(nums) - 2)


    def dp(self, nums, m_n_max, left, right):
        if m_n_max[left][right]:
            return m_n_max[left][right]
        
        if left > right: # nums[i:j] is empty set
            m_n_max[left][right] = 0
            return 0
             
        maximum = float("-inf")
        for i in range(left, right + 1):
            curr = nums[left - 1] * nums[i] * nums[right + 1] + self.dp(nums, m_n_max, left, i - 1) + self.dp(nums, m_n_max, i + 1 , right)
            maximum = max(maximum, curr)
        m_n_max[left][right] = maximum
        return maximum
    

    """
    - dp bottom-up: dp[i][j] = maximum coins bursting subset nums[i:j]
    - O(n^3), O(n^2)
    """
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        m_n_max = [[0] * len(nums) for _ in nums]
        
        for right in range(1, len(nums) - 1):
            for left in range(right, 0, -1):
                maximum = 0
                for i in range(left, right + 1):
                    curr = nums[left - 1] * nums[i] * nums[right + 1] + m_n_max[left][i - 1] + m_n_max[i + 1][right]
                    maximum = max(maximum, curr)
                m_n_max[left][right] = maximum
        return m_n_max[1][len(nums) - 2]