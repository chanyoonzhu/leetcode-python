import collections

# chars in t can be the same! So can't store in set, has to use dic

class Solution(object):
    def minWindow(self, s, t):

        l = r = minl = minr = 0
        minWin = len(s) + 1
        tDic = collections.Counter(list(t))
        tLen = len(tDic)
        currCnt = collections.defaultdict(int)
        matchChar = 0
        
        while r < len(s):
        
            while r < len(s):
                if s[r] in tDic:
                    currCnt[s[r]] += 1
                    if currCnt[s[r]] == tDic[s[r]]: # move r to right until get all chars
                        matchChar += 1
                        if matchChar == tLen:
                            break
                r += 1

            while matchChar == tLen: # move l to right until one char missing
                if s[l] in tDic:
                    currCnt[s[l]] -= 1
                    if currCnt[s[l]] < tDic[s[l]]:
                        matchChar -= 1
                l += 1
            l -= 1

            if matchChar + 1 == tLen and r - l + 1 < minWin: # first condition for r reach to end but not enough chars
                minWin = r - l + 1
                minl, minr = l, r
            
            r += 1; l += 1 # Don't forget to do this, or caught in loop
        
        if minWin > len(s):
            return ""
        else:
            return s[minl:minr+1]

sl = Solution()
print(sl.minWindow("ADOBECODEBANC", "ABC"))
print(sl.minWindow("aa", "aa"))

