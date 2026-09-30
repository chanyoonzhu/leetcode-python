# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

"""
- answer based on 157
- similar: 157-Read_N_Characters_Given_Read4
- difference: need to read many times, read4 may consume more char than needed in previous query, need to save the over-consumed chars somewhere for the next query to use
"""
class Solution:
    
    def __init__(self):
        self.remain = [] # stores remaining from last query
    
    def read(self, buf: List[str], n: int) -> int:
        buf_i = 0
        buf4 = [""] * 4
        need_read = n
        
        # consume remaining (not consumed due to n restriction) from previous read4 call
        if self.remain:
            consume_remain_count = min(len(self.remain), n)
            buf[buf_i:buf_i+consume_remain_count] = self.remain[:consume_remain_count]
            n -= consume_remain_count
            self.remain = self.remain[consume_remain_count:]
            buf_i += consume_remain_count
        
        while n > 0:
            read_4_count = read4(buf4)
            read_count = min(read_4_count, n)
            buf[buf_i:buf_i + read_count] = buf4[:read_count]
            buf_i += read_count
            
            # save remaining
            if n < read_4_count:
                self.remain = buf4[n:read_4_count]
                
            n -= read_count
            if read_4_count < 4:
                break

        return need_read - n

"""
- follow up: more efficient copy? when buf has enough space, use read4(buf)
"""
        