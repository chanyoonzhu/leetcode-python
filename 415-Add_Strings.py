class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        """
        - recursive
        - O(max(n1, n2)), O(max(n1, n2))
        """
        def add(idx1, idx2, res, carry):
            if idx1 < 0 and idx2 < 0:
                return res if not carry else str(carry) + res # don't forget the carry
            n1 = ord(num1[idx1]) - ord('0') if idx1 >= 0 else 0
            n2 = ord(num2[idx2]) - ord('0') if idx2 >= 0 else 0
            _sum = n1 + n2 + carry
            digit, carry = str(_sum % 10), _sum // 10
            return add(idx1 - 1, idx2 - 1, digit + res, carry)
        
        return str(add(len(num1) - 1, len(num2) - 1, "", 0))