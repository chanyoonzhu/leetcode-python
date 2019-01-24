class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        """
        - O(n), O(k)
        - replace when there's number closer than what is already in the candidate list 
        - not recommended
        """
        ans = []
        
        for n in arr:
            if len(ans) < k:
                ans.append(n)
            else:
                # left-most diff
                ld = abs(x - ans[0])
                # right-most diff
                rd = abs(x - ans[k-1])
                # current diff
                cd = abs(x - n)
                if ld > cd:
                    del ans[0]
                    ans.append(n)
        
        return ans
    
        """
        - O(n), O(n)
        - same idea, start from both ends (only ends values could have a larger distance)
        - recommended
        """
        
        ans = arr
        
        while len(ans) > k:
            if abs(x - ans[0]) > abs(x - ans[-1]):
                del ans[0]
            else:
                ans.pop()
        
        return ans
    
        """
        - O(logN), O(n)
        - binary search
        """
        
        ans = []
        l, r, mid = 0, len(arr) - 1, 0
        while l < r:
            mid = (l + r) / 2
            if x > mid:
                l = mid + 1
            else:
                r = mid
        
        # find position of x
        if r - k < 0:
            ans = arr[:k]
        else:
            ans = arr[r-k:r]
        
        # slide window
        while k > 0:
            if arr[r] < ans[0]:
                del ans[0]
                ans.append(arr[r])
                r += 1
            k -= 1
