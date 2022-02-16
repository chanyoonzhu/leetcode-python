"""
- binary search + backtracking
"""
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True) # assign jobs with longer time first
        lo, hi = max(jobs), sum(jobs)
        
        # backtracking
        def canFinish(idx):
            if idx == len(jobs): return True
            for i in range(len(cap)): # assign job at idx to each worker, try which one works
                if cap[i] >= jobs[idx]:
                    cap[i] -= jobs[idx] 
                    if canFinish(idx + 1):
                        return True
                    cap[i] += jobs[idx]
                if cap[i] == mid: # pruning otherwise TLE: cap[i] cannot be assigned anything to make this work, exit
                    break
            return False
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            cap = [mid] * k
            if canFinish(0):
                hi = mid
            else:
                lo = mid + 1
        return lo