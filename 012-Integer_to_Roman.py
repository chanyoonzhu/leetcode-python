class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        - solution 1
        - O(1) - The same number of operations is done, regardless of the size of the input
        - O(1)
        """
        result = ''
        roman_digits = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M', '', '',]]
        for one, five, ten in roman_digits:
            # digit, num = num % 10, num // 10
            num, digit = divmod(num, 10)
            curr = ''
            if digit <= 3:
                curr += one * digit
            elif digit == 4:
                curr += (one + five)
            elif digit <= 8:
                curr += (five + one * (digit - 5))
            elif digit == 9:
                curr += (one + ten)
            result = (curr + result)
        return result


        """
        - solution 2
        - O(1), O(1)
        """
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        def intToRoman(self, num: int) -> str:
            roman_digits = []
            # Loop through each symbol.
            for value, symbol in digits:
                # We don't want to continue looping if we're done.
                if num == 0: break
                count, num = divmod(num, value)
                # Append "count" copies of "symbol" to roman_digits.
                roman_digits.append(symbol * count)
            return "".join(roman_digits)
                
            
        
        
        
        
        