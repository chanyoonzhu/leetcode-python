class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        - O(n^2), O(n^2)
        - Brute force
        
        
        maxLen = 0
        for i in range(len(s)): #substring starting at i
            charSet = set()
            maxJ = i
            for j in range(i, len(s)):
                if s[j] not in charSet:
                    charSet.add(s[j])
                    if len(charSet) > 2:
                        maxJ = j-1
                        break
                maxJ = j
            maxLen = max(maxLen, maxJ-i+1)
        
        return maxLen
        """
    
        """
        - O(n), O(n)
        - Sliding window
        """
        dic = collections.defaultdict(int)
        maxLen = 0
        start = end = 0
        
        while end < len(s):
            dic[s[end]] += 1
            while len(dic) > 2 and start <= end:
                dic[s[start]] -= 1
                if dic[s[start]] == 0: # don't forget to remove key
                    del dic[s[start]]
                start += 1
            maxLen = max(maxLen, end-start+1)
            end += 1
            
        return maxLen
        

sl = Solution()
print(sl.lengthOfLongestSubstringTwoDistinct("bacc"))