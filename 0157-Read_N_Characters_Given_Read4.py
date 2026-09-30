"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

"""
- what does it mean - read the first n of chars into buffer (buf) using an API that's similar like read(buf, 4)
- key: terminates at two conditions: 1. do not read if completes n char 2. do not read if no more file to read - when read4(buf4) returns < 4
- O(n), O(1)
"""
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf_i = 0
        buf4 = [""] * 4
        need_read = n
        
        while n:
            read_4_count = read4(buf4)
            read_count = min(read_4_count, n)
            buf[buf_i:buf_i + read_count] = buf4[:read_count]
            buf_i += read_count
            n -= read_count # do not read if completes n char
            if read_4_count < 4: # do not read if no more file to read
                break
            
        return need_read - n # total read = need_read - cannot read

        """
        C and C++ have faster implementations which avoids double copy
        O(n),O(1)
        """