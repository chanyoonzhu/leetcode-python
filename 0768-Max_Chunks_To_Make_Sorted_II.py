"""
- linear scan
- intuition: Iterate through the array, each time all elements to the left are smaller (or equal) to all elements to the right (left max of nums[:i] <= right min of nums[i:]), there is a new chunck
- O(n), O(n)
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        left_max, right_min = [], []
        n = len(arr)
        res = 0
        for i in range(n):
            if left_max and left_max[-1] > arr[i]:
                left_max.append(left_max[-1])
            else:
                left_max.append(arr[i])
            if right_min and right_min[0] < arr[n-1-i]:
                right_min.insert(0, right_min[0])
            else:
                right_min.insert(0, arr[n-1-i])
                
        for i in range(n-1):
            if left_max[i] <= right_min[i+1]:
                res += 1
        return res + 1

"""
- monotonically increasing stack
- O(n), O(n)
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        mono_stack = [] # mono_increasing: keeps the max of each chunck
        for num in arr:
            largest = num
            while mono_stack and mono_stack[-1] > num: # when max of prev chunk larger than next number, merge number to chunk
                largest = max(largest, mono_stack.pop())
            mono_stack.append(largest)
        
        return len(mono_stack)