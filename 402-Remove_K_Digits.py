class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        """
        s = ['0']
        idx = 0
        for i in range(len(num)):
            while s and k and ord(num[i]) < ord(s[-1]):
                s.pop()
                k = k - 1
            s.append(num[i])  
            
        while k > 0:
            s.pop()
            k = k - 1
            
        while len(s) > 1 and s[0] == '0':
            s.pop(0)
            k = k - 1
        return ''.join(s)
        """
        
        """
        - O(kn)
        """
        while k > 0:
            idx = 0
            while idx + 1 < len(num) and num[idx] <= num[idx+1] :
                idx += 1
            num = num[:idx] + num[idx+1:]
            k -= 1
        num = num.lstrip('0')
        return num if num != "" else "0"

        """
        - O(n)
        """
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'

s = Solution()
print(s.removeKdigits('1234567890', 9))
        
            