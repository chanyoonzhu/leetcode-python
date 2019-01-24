class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
        - O(n^3), O(n^3)
        - exceed time limit
        - pick all possible starting and ending positions for a substring, and verify if it is a palindrome.
        
        
        """
        def isPalindrome(t):
            reverse = t[::-1]
            return t == reverse
     
        longestLen = currLen = 0
        start = end = 0
        for i in range(len(s)):
            for k in range(len(s), i, -1):
                if isPalindrome(s[i:k]):
                    currLen = k - i
                    if currLen > longestLen:
                        longestLen = currLen
                        start, end = i, k
                    break #others starting at the same index position cannot be longer than this one
        return s[start:end]
        
    
        """
        - O(n^2), O(n^2)
        - Reverse SS and become S'S. Find the longest common substring between SS and S'S. Check indices
        """

        """
        - O(n^2), O(n^2)
        - Dynamic Programming
        dp[i][j] keeps track of whether s[i:j+1] is a palindrome
        
        dp = [[0] * len(s) for _ in range(len(s))]
        max_len = 0
        start = end = 0
            
        for i in range(len(s)-1, -1, -1): # starting from bottom right corner
            for j in range(i, len(s)): 
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start, end = i, j + 1
        
        return s[start:end]
        """
        
        """
        - O(n^2), O(n^2)
        - starting from the middle
        - draft version
        
        max_len = 0
        start = end = 0
        
        for i in range(len(s)):
            distance = 0
            # odd palindrome
            while i - distance >= 0 and i + distance < len(s) and s[i-distance] == s[i+distance]:
                palindrome_len = distance * 2 + 1
                if palindrome_len > max_len:
                    max_len = palindrome_len
                    start, end = i - distance, i + distance
                distance += 1
            # even palindrome
            distance = 0
            if i + 1 < len(s) and s[i] == s[i+1]:
                while i - distance >= 0 and i + 1 + distance < len(s) and s[i-distance] == s[i+1+distance]:
                    palindrome_len = distance * 2 + 2
                    if palindrome_len > max_len:
                        max_len = palindrome_len
                        start, end = i - distance, i + 1 + distance
                    distance += 1
        return s[start:end+1]
        """
        
        """
        - O(n^2), O(n^2)
        - starting from the middle
        - improved version
        - source: https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
        
        ans = ""
        
        def findLocalPalindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r] # don't forget to go back one index
        
        for i in range(len(s)):
            # odd palindrome
            p = findLocalPalindrome(s, i, i)
            if len(p) > len(ans):
                ans = p
            # even palindrom
            p = findLocalPalindrome(s, i, i+1)
            if len(p) > len(ans):
                ans = p
        
        return ans
        """
        
        """
        O(n), O(1)
        - Manache's Algorithm (using mirror feature of a palindrome)
        - not finished
        ""
