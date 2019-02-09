class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """


        """
        - A hard problem since it has a lot of corner cases
        - intuition: deal with a group of three numbers at a time
        - corner cases:
            # 11-19
            # 1000,000 is "One Million" not "One Million Thousand"
            # zeros
        """

        thousands = ["Thousand", "Million", "Billion"]
        tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tenToTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        
        res = []
        
        i = j = 0 # i is index in this group, j is group index
        oneTemp = 0 # temporarily hold the ones digit of this group incase tens needs it
        while num:
            if i == 0 and j > 0:
                if j > 1 and res[0] == thousands[j-2]: res.pop(0) # incase the previous group is all zero, get rid of the previous thousands
                res.insert(0, thousands[j-1])
            num, digit = divmod(num, 10)
            if i == 0:
                oneTemp = digit
                if digit: res.insert(0, ones[digit-1]) # if for zero
            elif i == 1:
                if digit == 1: # 11-19
                    if oneTemp: res.pop(0) # if for oneTemp == 0
                    twoDigits = digit * 10 + oneTemp
                    res.insert(0, tenToTwenty[twoDigits-10])
                else:
                    if digit: res.insert(0, tens[digit-1]) # if for zero
            elif i == 2 and digit:
                res.insert(0, ones[digit-1] + " Hundred")
            if i == 2: j += 1
            i = 0 if i == 2 else i + 1
                
        return ' '.join(res) if res else "Zero" # zero for input 0

        """
        - recursive
        check out : https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python
        """

sl = Solution()
print(sl.numberToWords(2345))