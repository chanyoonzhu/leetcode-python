class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        """
        O(n^2), O(n^2)?
        - obvious solution
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        temp, output = [], []
        
        for d in digits:
            if output:
                temp = [w + l for l in mapping[d] for w in temp]
            else:
                temp = mapping[d]
            output = temp[:] # deep copy for immutable objects
            
        return output
        """

        """
        - less memory
        
        if len(digits) == 0 or not digits:
            return []
        
        self.ans = [""]
        
        dic = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        for d in digits:
            prevLen = len(self.ans)
            for i in range(len(dic[d])-1):
                added = [item + dic[d][i+1] for item in self.ans[:prevLen]]
                self.ans.extend(added)
            for i in range(prevLen):
                self.ans[i] += dic[d][0]
                
        return self.ans
        """
        
        
    
    
        """
        - dfs
        
        """
        
        if len(digits) == 0 or not digits:
            return []
        
        self.ans = []
        dic = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        def helper(digits, res):
            
            if len(digits) == 0:
                self.ans.append(res)
            else:
                for d in dic[digits[0]]:
                    helper(digits[1:], res + d)
            
        helper(digits, "")
        return self.ans

print(Solution().letterCombinations('23'))