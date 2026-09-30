"""
- queue
- O(n), O(k)
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        res = deque(arr[n-k:])
        for i in range(len(arr)-k-1, -1, -1): # from right to left to pick up same dist with smaller index
            if abs(arr[i] - x) <= abs(res[-1] - x):
                res.pop()
                res.appendleft(arr[i])
            else:
                break
        return res
    
"""
- O(logN), O(n)
- binary search
"""   
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
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
