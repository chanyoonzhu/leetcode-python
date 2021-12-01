"""
- prefix sum + hashmap
- O(n), O(n)
"""
class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        result = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                result = i + 1
            elif score - 1 in seen: # intuition: sum(hours[seen[score - 1]: i + 1]) = 1
                result = max(result, i - seen[score - 1])
            if score not in seen: # only store first occurrence to get the smallest index for a score
                seen[score] = i
        return result

"""
- monotonically increasing/decreasing stack
- intuition: convert to prefix sum array, need to find the longest subarray where i < j and prefix[i] < prefix[j] (number > 8 more than number <= 8)
- similar: 962-Maximum Width Ramp
- O(n), O(n)
"""
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        prefixes = [0]
        for x in hours:
            num = 1 if x > 8 else -1
            prefixes.append(prefixes[-1] + num)
        
        stack = []
        res = 0
        for i in range(len(prefixes)):
            if not stack or prefixes[i] < prefixes[stack[-1]]: # only append left boundary candidate to stack
                stack.append(i)
                
        for i in range(len(prefixes) - 1, -1, -1): # greedily search from the right boundary with the largest index
            while stack and prefixes[i] > prefixes[stack[-1]]:
                res = max(res, i - stack.pop())
            if not stack:
                break
                
        return res