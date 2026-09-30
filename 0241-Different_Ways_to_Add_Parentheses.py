"""
- dp (top-down)
- O(n^3), O(n^3)?
"""
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        mem = {}
        
        def helper(x, y, op):
            if op == "+":
                return x + y
            elif op == "-":
                return x - y
            elif op == "*":
                return x * y
        
        def dfs(input):
            if input in mem:
                return mem[input]
            if input.isdigit():
                mem[input] = [int(input)]
                return mem[input]
            result = []
            for i, c in enumerate(input):
                if c in ['+', '-', '*']:
                    l = dfs(input[:i])
                    r = dfs(input[i + 1:])
                    result.extend([helper(x, y, c) for x in l for y in r])
            mem[input] = result
            return result
        
        return dfs(expression)

"""
- dp (bottom-up)
- O(n^3), O(n^3)?
"""
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def helper(x, y, op):
            if op == "+":
                return x + y
            elif op == "-":
                return x - y
            elif op == "*":
                return x * y
        
        ops = []
        nums = []    
        num = 0
        for i, c in enumerate(expression):
            if c in ['+', '-', '*']:
                nums.append(num)
                num = 0
                ops.append(c)
            else:
                num = num * 10 + ord(c) - ord('0')
        nums.append(num)
        
        n = len(nums)
        dp = [[None] * n for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i] = [nums[i]]
            for j in range(i - 1, -1, -1):
                dp[j][i] = []
                for k in range(j, i):
                    dp[j][i].extend(helper(x, y, ops[k]) for y in dp[k + 1][i] for x in dp[j][k])
        return dp[0][n - 1]
                