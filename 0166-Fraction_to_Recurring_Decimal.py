"""
- long division with hashmap
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        POS, NEG = "", "-"
        div, mod = divmod(numerator, denominator)
        if mod == 0: return div
        
        sign = POS if (numerator == abs(numerator)) is (denominator == abs(denominator)) else NEG
        numerator, denominator = abs(numerator), abs(denominator)
        div = div if sign == POS else -div
        
        result = sign + str(div) + '.'
        rem_positions = {}
        
        rem = numerator % denominator
        current_quotient = []
        i = 0 # rem pos
        
        while rem != 0:
            rem_positions[rem] = i
            current_quotient.append(str(rem * 10 // denominator))
            rem = rem * 10 % denominator
            i += 1
            if rem in rem_positions:
                pos = rem_positions[rem]
                current_quotient.insert(pos, "(")
                current_quotient.append(")")
                break
            
        return result + "".join(current_quotient)