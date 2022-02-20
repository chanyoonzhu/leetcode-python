"""
- hashmap
- O(n), O(1)
- two passes
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        guess_to_counts = defaultdict(int)
        for i, x in enumerate(guess):
            if x == secret[i]:
                bulls += 1
            else:
                guess_to_counts[x] += 1
        
        for i, x in enumerate(secret):
            if x == guess[i]:
                continue
            if guess_to_counts[x] > 0:
                cows += 1
                guess_to_counts[x] -= 1
        
        return str(bulls) + "A" + str(cows) + "B"
    
        
"""
- hashmap
- O(n), O(1)
- one pass
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        counts = [0] * 10
        
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                if counts[s] < 0: # has guessed char s before i
                    cows += 1
                if counts[g] > 0: # has secret char g before i
                    cows += 1
                counts[s] += 1
                counts[g] -= 1
            
        return str(bulls) + 'A' + str(cows) + 'B'
        
        
        