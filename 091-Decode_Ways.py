class Solution(object):
    total = 0
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        - wrong answer -  "2101" output: 3 expected: 1
        """
        
        ways = [0] * len(s)
        s_list = [(ord(l) - ord("0")) for l in s]
        if len(s_list) > 0 and s_list[0] != 0:
            ways[0] = 1
        for i in range(1, len(s_list)):
            if s_list[i-1] * 10 + s_list[i] <= 26 and s_list[i] != 0:
                ways[i] = ways[i-1] + 1
            else:
                ways[i] = ways[i-1]
        return ways[-1]

        class Solution(object):  

    """
    - dfs with memoization: can either parse one or two digits at a time, therefore a tree
    - O(n): Memoization helps in pruning the recursion tree and hence decoding for an index only once
    - O(n): The recursion stack would also be equal to the length of the string (when skewed)
    """

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.dfs(s, 0, dict())

        
    def dfs(self, s, i, mem): # use index to track substring to save space
        if i in mem:
            return mem[i] # use index rather than string as hash key to save space

        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        
        ways = self.dfs(s, i+1, mem) # can always parse only one digit (if not zero, which already checked in above)
        if i + 2 <= len(s) and int(s[i:i+2]) <= 26: # parse when have more then two digits left and first two are less or equal than 26:
            ways += self.dfs(s, i+2, mem)
            
        mem[i] = ways
        return ways

    """
    - dp: dp[i] is number of ways to parse s[:i], similar to "climb stairs" (with conditions)
    - O(n), O(n) - space can be optimized to O(1) since in each iteration only need to track dp[i-1] and dp[i-2]
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1] + [0] * (len(s)) # add a dummy value at the beginning
        for i in range(1, len(s)+1):
            if s[i-1] != "0": # can consume as single digit when is not zero
                dp[i] = dp[i-1]
            if i-2 >= 0 and int(s[i-2:i]) <= 26 and s[i-2] != "0": # # can consume together with previous digit if less than 26 and previous is not zero
                dp[i] += dp[i-2]
        return dp[-1]
