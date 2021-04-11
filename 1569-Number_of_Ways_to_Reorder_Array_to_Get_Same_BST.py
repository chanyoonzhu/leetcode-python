class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        """
        - dfs (preorder)
        - O(n * n * O(comb)), O(n)
        - intuition: Two subtrees of the same level can combine in any order as long as the order in each sub tree keeps unchanged. 
        """

        """ combination implementation
        @lru_cache(None)
        def comb(n,k):
            if k == 0:
                return 1
            elif n < k:
                return 0
            else:
                return comb(n-1,k-1) + comb(n-1,k)
        """

        def dfs(sub):
            if not sub:
                return 1
            left = [num for num in sub if num < sub[0]]
            right = [num for num in sub if num > sub[0]]
            # ways of selecting spots for nums smaller than sub root (equals to says of selecting spots for nums larger than sub root)
            combinations = math.comb(len(left) + len(right), len(left)) 
            left_combinations = dfs(left)
            right_combinations = dfs(right)
            return left_combinations * right_combinations * combinations
        
        mod = 10 ** 9 + 7
        return (dfs(nums) - 1) % mod