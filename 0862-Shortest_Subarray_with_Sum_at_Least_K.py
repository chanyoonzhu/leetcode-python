"""
- brute force
- O(n^2), O(n)
- TLE
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixes = [0]
        for n in nums:
            prefixes.append(prefixes[-1] + n)
            
        N = len(prefixes)
        result = N
        for i in range(N):
            for j in range(i + 1, N):
                if prefixes[j] - prefixes[i] >= k:
                    result = min(result, j - i)
        return result if result < N else -1

"""
- monotonic queue 
- more complex version of 209-Minimum Size Subarray Sum, has negative nums and cannot just increase left index to find smaller window
- q: stores the indexes of possible left index (i) of subarray, with prefix[i] increasing
- O(n), O(n)
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixes = [0]
        for n in nums:
            prefixes.append(prefixes[-1] + n)
            
        N = len(prefixes)
        result = N
        q = collections.deque()
        q.append(0)
        for i in range(1, N):
            while q and prefixes[q[-1]] >= prefixes[i]: # greedily pop previous indexes with a larger prefix sum
                q.pop()
            q.append(i)
            while q and prefixes[i] - prefixes[q[0]] >= k: # prefixes[i] - prefixes[q[0]] always has the highest chance of >=k since prefixes[q[0]] is the smallest
                result = min(result, i - q[0])
                q.popleft()
        return result if result < N else -1