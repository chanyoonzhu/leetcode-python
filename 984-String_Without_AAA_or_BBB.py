class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        res = []
        freqs = list(zip([a, b], ['a', 'b']))
        if freqs[0][0] < freqs[1][0]:
            freqs[0], freqs[1] = freqs[1], freqs[0]
            
        high_freq, low_freq, high_c, low_c = freqs[0][0], freqs[1][0], freqs[0][1], freqs[1][1]
        res = [high_c + low_c] * low_freq # consume one high_c and one low_c
        high_freq -= low_freq
        i = 0
        while high_freq and i < len(res): # consume rest high_c
            res[i] = high_c + res[i]
            i += 1
            high_freq -= 1
        if high_freq: # don't forget the end
            res.extend([high_c] * high_freq)
            
        return ''.join(res)