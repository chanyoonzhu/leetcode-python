class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        cbn = k ** n
        
        ans = ['0'] * n
        
        allPasswords = set(['0' * n])
        
        self.dfs(ans, allPasswords, k, n, cbn)
        
        return ''.join(ans)
        
        
    def dfs(self, password, allPasswords, k, n, cbn):
        if len(allPasswords) == cbn:
            return True
        for i in range(k):
            nextPassword = ''.join(password[len(password)-n+1:]) + str(i)
            if nextPassword not in allPasswords:
                password.append(str(i))
                allPasswords.add(nextPassword)
                if self.dfs(password, allPasswords, k, n, cbn):
                    return True
                allPasswords.remove(nextPassword)
                password.pop()
        return False
                
print(Solution().crackSafe(1, 2))