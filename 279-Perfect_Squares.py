class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        - dynamic programming, with squares computed on the fly
        - O(n * sqrt(n))
        - o(n)
        """
        square_nums = [0] * n
        square_root = 1
        squares = [1]
        for i in range(n):
            if i + 1 == squares[-1]:
                square_nums[i] = 1
                square_root += 1
                squares.append(square_root ** 2)
            else:
                minimum_num = float("inf")
                for square in squares[:-1]:
                    minimum_num = min(minimum_num, square_nums[i - square] + 1)
                square_nums[i] = minimum_num
        return square_nums[-1]

        """
        - similar with pre-computed squares
        """
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)
                    