"""
- string parsing
- key:
    If char == + or char == -, then prev char (if there is) must be e
    . cannot appear twice or after e
    e cannot appear twice, and there must be at least one digit before and after e
    All other non-digit char is invalid
"""
"""
examples:
valid: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
invalid: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        found_dot = found_e = found_digit = False
        for i, c in enumerate(s):
            if c in '+-':
                # need to be sign (index == 0) or after e/E
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c == '.':
                if found_dot or found_e: return False
                found_dot = True
            elif c in 'eE':
                if found_e or not found_digit:
                    return False
                found_e, found_digit = True, False
            elif c.isdigit():
                found_digit = True
            else:
                return False
        return found_digit

"""
- Deterministic Finite Automaton
"""
class Solution(object):
    def isNumber(self, s):
        # This is the DFA we have designed above
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]
        
        current_state = 0
        for c in s:
            if c.isdigit():
                group = "digit"
            elif c in ["+", "-"]:
                group = "sign"
            elif c in ["e", "E"]:
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False

            if group not in dfa[current_state]:
                return False
            
            current_state = dfa[current_state][group]
        
        return current_state in [1, 4, 7]