"""
- similar: 2007-Find_Original_Array_From_Doubled_Array
"""
"""
- greedy + hashmap
- O(n), O(n)
"""
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        N = len(arr)
        if N % 2: return False
        counter = Counter(arr)
        if counter[0] % 2: return False
        
        for x in sorted(counter, key=lambda x: abs(x)):
            cur_count = counter[x]
            if cur_count > counter[2 * x]:
                return False
            counter[2 * x] -= counter[x]
            counter[x] = 0
        return sum(counter.values()) == 0