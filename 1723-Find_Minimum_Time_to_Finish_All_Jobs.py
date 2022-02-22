"""
- binary search + backtracking
- TLE
"""
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:       
        
        def canComplete(i, available_times):
            if i == len(jobs):
                return True
            for j in range(len(available_times)):
                if available_times[j] >= jobs[i]:
                    available_times[j] -= jobs[i]
                    if canComplete(i + 1, available_times):
                        return True
                    available_times[j] += jobs[i]
            return False
            
        
        lo, hi = max(jobs), sum(jobs)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if canComplete(0, [mid] * k):
                hi = mid
            else:
                lo = mid + 1
        return lo

"""
- binary search + backtracking
- with pruning
"""
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:       
        
        def canComplete(i, available_times, max_time):
            if i == len(jobs):
                return True
            for j in range(len(available_times)):
                if available_times[j] >= jobs[i]:
                    available_times[j] -= jobs[i]
                    if canComplete(i + 1, available_times, max_time):
                        return True
                    available_times[j] += jobs[i]
                if available_times[j] == max_time: # pruning: cap[i] cannot be assigned any job to make this work, exit
                    return False
            return False
            
        jobs.sort(reverse=True) # assign large job first
        lo, hi = max(jobs), sum(jobs)
        while lo < hi:
            mid = lo + (hi - lo) // 2  
            if canComplete(0, [mid] * k, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo