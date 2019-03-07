class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        """
        - O(n)
        - Hashtable
        
        bulls = cows = 0
        table = collections.Counter(list(secret));
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                table[guess[i]] -= 1
                if table[guess[i]] == 0:
                    del table[guess[i]]
        
        for i in range(len(secret)): 
            if secret[i] != guess[i] and guess[i] in table:
                cows += 1
                table[guess[i]] -= 1
                if table[guess[i]] == 0:
                    del table[guess[i]]
        
        return str(bulls) + 'A' + str(cows) + 'B'
        """
        
        """
        - O(n), O(1)
        - number array
        
        bulls = cows = 0
        numbersS = [0] * 10
        numbersG = [0] * 10
        
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                numbersS[s] += 1
                numbersG[g] += 1
                
        for i in range(10):
            cows += min(numbersS[i], numbersG[i])
            
        return str(bulls) + 'A' + str(cows) + 'B'
        """
        
    
        
        """
        - O(n), O(1)
        - number array one pass
        """
        bulls = cows = 0
        numbers = [0] * 10
        
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                if numbers[s] < 0:
                    cows += 1
                if numbers[g] > 0:
                    cows += 1
                numbers[s] += 1
                numbers[g] -= 1
            
        return str(bulls) + 'A' + str(cows) + 'B'
        
        
        