"""
- greedy + hashmap
- caveat: [2,4,8] which pair to match? always start from smaller numbers
"""
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        result = []
        if counter[0] % 2: # odd number of 0
            return []
        else:
            result.extend([0] * (counter[0]//2))
            
        for x in sorted(counter): # greedily match smaller number
            if counter[x] > counter[2 * x]:
                return []
            if x:
                counter[2 * x] -= counter[x]
                result.extend([x] * counter[x])
            
        return result