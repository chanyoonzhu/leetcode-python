"""
- two pointers
- O(m + n), O(m + n)
"""
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i1 = i2 = 0
        prod_encoded = []
        while i1 < len(encoded1) and i2 < len(encoded2):
            num1, freq1 = encoded1[i1]
            num2, freq2 = encoded2[i2]
            
            prod = num1 * num2
            prod_freq = min(freq1, freq2)
            
            encoded1[i1][1] -= prod_freq
            encoded2[i2][1] -= prod_freq
            
            if encoded1[i1][1] == 0:
                i1 += 1
                
            if encoded2[i2][1] == 0:
                i2 += 1
                            
            if not prod_encoded or prod_encoded[-1][0] != prod:
                prod_encoded.append([prod, prod_freq])
            else:
                prod_encoded[-1][1] += prod_freq
            
        return prod_encoded