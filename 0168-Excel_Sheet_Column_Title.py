class Solution:
    def convertToTitle(self, n: int) -> str:

        """
        - a medium hard one, different from 26hex
        """
        a = ord('A')
        alphabet=[chr(i) for i in range(a,a+26)]
        
        ans = ''
        while n > 0:
            n, r = divmod(n-1, 26) # n-1 is key
            ans = alphabet[r] + ans
            
        
        return ans
        
s = Solution()
s.convertToTitle(701)