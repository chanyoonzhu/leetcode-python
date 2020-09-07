class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        - backtracking with set, cannot be further optimized using memoization, can't use greedy (dp won't optimize computing time)
        - O(2^n)
        - O(2^n)
        """
        unique = ['']
        for word in arr:
            for concat in unique:
                temp = word + concat
                if len(temp) == len(set(temp)):
                    unique.append(temp)
        return max([len(concat) for concat in unique])
        