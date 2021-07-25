"""
- binary search + backtracking
"""
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True) # assign jobs with longer time first
        lo, hi = max(jobs), sum(jobs)
        
        def canFinish(time, assigned, idx):
            if idx == len(jobs): return True
            for i in range(len(assigned)):
                assigned[i] += jobs[idx]
                if assigned[i] <= time and canFinish(time, assigned, idx + 1):
                    return True
                assigned[i] -= jobs[idx]
                if assigned[i] == 0: # if assigning to an empty bucket won't work, assigning the same task to other buckets won't work too. without this will be TLE
                    break
            return False
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            assigned = [0] * k
            if canFinish(mid, assigned, 0):
                hi = mid
            else:
                lo = mid + 1
        return lo