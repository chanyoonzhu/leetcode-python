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

"""
- O(n), O(n)
split, reverse, then join 
note: word[::-1] copies a list and did not reverse in place, you need to write your own code to reverse in place
- O(n), O(1)
reverse whole string, then reverse each word
not possible in Python because strings are immutable. Can be accomplished if passing in a list of chars
"""
class Solution:
    def reverseWords(self, s_list: [str]) -> str:
        left, right = 0, len(s_list) - 1
        # reverse whole string
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left, right = left + 1, right - 1
        w_left, w_right = 0, 0
        while w_left < len(s_list):
            while w_left < len(s_list) and s_list[w_left] == ' ':
                del s_list[w_left] # remove leading spaces
            while w_right < len(s_list) and s_list[w_right] != ' ':
                w_right += 1 # find word end
            # reverse workd
            slow, fast = w_left, w_right - 1
            while slow < fast:
                s_list[slow], s_list[fast] = s_list[fast], s_list[slow]
                slow, fast = slow + 1, fast - 1
            if w_right < len(s_list):
                w_right += 1 # skip one space
            w_left = w_right # reset next word start
        if len(s_list) > 0 and s_list[-1] == ' ': # handle space in the end
            del s_list[-1]
        return "(" + ''.join(s_list) + ")"

s = Solution()
print(s.reverseWords([' ', ' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', ' ', ' ']))
print(s.reverseWords([' ', 'h', 'e', 'l', 'l', 'o', ' ', ' ', 'w', 'o', 'r', 'l', 'd', '!', ' ']))
print(s.reverseWords(['h', 'e', 'l', 'l', 'o', ' ', ' ', 'w', 'o', 'r', 'l', 'd', '!']))
print(s.reverseWords(['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '!']))
print(s.reverseWords([' ', 'h', 'e', 'l', 'l', 'o', ' ', ' ', 'w', 'o', 'r', 'l', 'd', '!']))
print(s.reverseWords(['h', 'e', 'l', 'l', 'o', ' ', ' ', 'w', 'o', 'r', 'l', 'd', '!', ' ']))
print(s.reverseWords([' ', ' ']))

class Solution2:
    def reverseWords(self, s):       
        chars = [t for t in s]
        slow, n = 0, len(s)
        for fast in range(n):
            if chars[fast] != " " or (fast > 0 and chars[fast] == " " and chars[fast-1] != " "):
                chars[slow] = chars[fast]
                slow += 1
                
        if slow == 0: return ""       
        chars = chars[:slow-1] if chars[-1] == " " else chars[:slow]
        chars.reverse()
        
        slow, m = 0, len(chars)
        for fast in range(m + 1):
            if fast == m or chars[fast] == " ":
                chars[slow:fast] = chars[slow:fast][::-1]
                slow = fast + 1
                
        return "(" + "".join(chars) + ")"

s2 = Solution2()
print(s2.reverseWords("  hello world!  "))