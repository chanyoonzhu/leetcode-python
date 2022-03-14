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
        
        below20 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        def helper(num):
            if num == 0:
                return []
            if num < 20:
                return [below20[num-1]]
            if num < 100:
                return [tens[num//10-2]] + helper(num%10)
            if num < 1000:
                return [below20[num//100-1]] + ['Hundred'] + helper(num%100)
            else:
                for p, w in enumerate(['Thousand', 'Million', 'Billion']):
                    if num < 1000 ** (p+2):
                        return helper(num//1000 ** (p+1)) + [w] + helper(num%1000 ** (p+1))
                
        return ' '.join(helper(num)) if num != 0 else 'Zero'

"""
- O(logn)
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        groups = ["Thousand", "Million", "Billion", "Trillion"]
        ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ten_to_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        def hundredToWords(num):
            if not num:
                return ""
            if num < 10:
                return ones[num-1]
            elif 10 <= num < 20:
                return ten_to_twenty[num-10]
            elif num < 100:
                ten, one = divmod(num, 10)
                print_tens = tens[ten-2]
                if one: 
                    print_tens += " " + ones[one-1]
                return print_tens
            else:
                hundred, mod = divmod(num, 100)
                print_mod = hundredToWords(mod)
                print_hundred = ones[hundred-1] + " Hundred"
                if print_mod: print_hundred += " " + print_mod
                return print_hundred

        group_i = -1
        group_size = 1000
        res = ""
        while num:
            num, mod = divmod(num, group_size)
            group_print = hundredToWords(mod)
            if group_i >= 0 and group_print:
                res = group_print + f" {groups[group_i]}" + ((" " + res) if res else "")
            else:
                res = group_print + res
            group_i += 1
        return res if res else "Zero"

sl = Solution()
print(sl.numberToWords(2345))