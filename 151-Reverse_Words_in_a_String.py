class Solution:
    def reverseWords(self, s: str) -> str:
        
        """
        split() compresses consecutive white spaces while split(' ') splits with exactly one space
        """

        """
        - O(n), O(n)
        
        words = s.split(' ')
        words = [word for word in words if word != '']
        words = words[::-1]
        return ' '.join(words)
        """
        
        """
        - slow 
        
        import re
        words = re.findall(r'\S+', s)
        words = words[::-1]
        return ' '.join(words)
        """
        
        """
        reversed = ''
        words = s.split(' ')
        for word in words:
            if word != '':
                reversed = word + ' ' + reversed
        return reversed.rstrip()
        """

        """
        words = s.split()
        words = reversed(words)
        return ' '.join(words)
        """
        
    
    
        return ' '.join(reversed(s.split()))