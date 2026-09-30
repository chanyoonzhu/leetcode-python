"""
- stacks
- O(nlogn), O(n)
- todo: answer copied
"""
class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        next_odd, next_even = [0] * n, [0] * n

        stack = [] # indexes waiting to find next higher/lower, in the order of arr[index] sorted
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_odd[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_even[stack.pop()] = i
            stack.append(i)

        odd, even = [0] * n, [0] * n
        odd[-1] = even[-1] = 1
        for i in range(n - 2, -1, -1):
            odd[i] = even[next_odd[i]]
            even[i] = odd[next_even[i]]
        return sum(odd)
                
            
            
        
        
        
            
            
        