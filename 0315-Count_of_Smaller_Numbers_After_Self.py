class Solution:

    """
    - binary search with an additional sorted array
    - O(n^2logn), O(n)
    - exceed time limit
    """
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        nums_sorted = []
        smaller_counts = []
        
        def binary_search(n, left, right):
            if left == right:
                return left
            mid = left + (right - left + 1) // 2
            if nums_sorted[mid] >= n:
                return binary_search(n, left, mid - 1)
            else:
                return binary_search(n, mid, right)
            
        
        def find_smaller_counts_and_insert(n):
            idx = binary_search(n, -1, len(nums_sorted) - 1) if nums_sorted else -1 
            nums_sorted.insert(idx + 1, n)
            return idx + 1
        
        
        for i in range(len(nums) - 1, -1, -1):
            counts = find_smaller_counts_and_insert(nums[i])
            smaller_counts.insert(0, counts)
        return smaller_counts
    

"""
- merge sort: merge sort the array, for an item j, whenever an element on its right move to its left during merge, increase the count of j by 1
- O(nlogn), O(n)
"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        self.merge_sort(nums, [i for i in range(N)],  0, N - 1, res)
        return res
        
    def merge(self, nums, indexes, left, mid, right, smallers):
        p1, p2 = left, mid + 1
        merged = []
        while p1 <= mid and p2 <= right:
            if nums[indexes[p1]] <= nums[indexes[p2]]:
                merged.append(indexes[p1])
                smallers[indexes[p1]] += (p2 - (mid + 1)) # p2 - (mid + 1) elements after mid already merged before p1 merges, so p2 - (mid + 1) elements smaller then p1
                p1 += 1
            else:
                merged.append(indexes[p2])
                p2 += 1
        while p1 <= mid:
            merged.append(indexes[p1])
            smallers[indexes[p1]] += (p2 - (mid + 1)) # easy to miss this step
            p1 += 1
        while p2 <= right:
            merged.append(indexes[p2])
            p2 += 1
        indexes[left:right+1] = merged
        
    def merge_sort(self, nums, indexes, left, right, smallers):
        if left < right:
            mid = left + (right - left) // 2
            self.merge_sort(nums, indexes, left, mid, smallers)
            self.merge_sort(nums, indexes, mid + 1, right, smallers)
            self.merge(nums, indexes, left, mid, right, smallers)
