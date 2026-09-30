"""
- cache
- O(n*4^n), O(n^2)
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        for d in digits:
            cur_result = []
            if not result:
                cur_result = letters[d]
            else:
                cur_result = [w + c for c in letters[d] for w in result]
            result = cur_result
        return result 

"""
- backtracking
- O(n*4^n), O(n^2)
"""  
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(i, output):
            if i == len(digits):
                return output
            if not output: 
                temp = letters[digits[i]]
            else:
                temp = [w + c for c in letters[digits[i]] for w in output]
            return backtrack(i + 1, temp)
            
        return backtrack(0, [])

print(Solution().letterCombinations('23'))
