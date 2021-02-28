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
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        indexes = [i for i in range(len(nums))]
        counts = [0] * (len(nums))
        
        def merge(start, mid, end, indexes, counts):
            i, j = start, mid + 1
            merged = []
            while mid >= i and end >= j:
                if nums[indexes[i]] <= nums[indexes[j]]:
                    merged.append(indexes[i])
                    # Whenever we add an item from the left array to the result, 
					# we must have seen j - (mid + 1) smaller items from the right, which 
					# have higher index in the original array.
                    counts[indexes[i]] += (j - (mid + 1)) 
                    i += 1
                else:
                    merged.append(indexes[j])
                    j += 1
            if mid >= i:
                merged.extend(indexes[i:mid + 1])
                for i in range(i, mid + 1):
                    counts[indexes[i]] += (j - (mid + 1))
            if end >= j:
                merged.extend(indexes[j:end + 1])
            indexes[start:end + 1] = merged
                
        def merge_sort(start, end, indexes, counts):
            if start < end:
                mid = start + (end - start) // 2
                merge_sort(start, mid, indexes, counts)
                merge_sort(mid + 1, end, indexes, counts)
                merge(start, mid, end, indexes, counts)
        
        merge_sort(0, len(nums) - 1, indexes, counts)
        return counts
