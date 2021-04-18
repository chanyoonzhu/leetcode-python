class TopVotedCandidate:

    """
    - binary search - with bisect
    - O(n + Qlogn), O(n) Q - number of queries
    """
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.counter = collections.Counter()
        self.top_candidate_at_time = self.calculate_top_candidate_at_time()

    def q(self, t: int) -> int:
        idx = bisect.bisect(self.times, t) - 1
        return self.top_candidate_at_time[idx]
        """ self implemented binary search
        i, j = 0, len(self.times) - 1
        while i < j:
            mid = i + (j - i + 1) // 2
            if self.times[mid] == t:
                return self.top_candidate_at_time[mid]
            elif self.times[mid] > t:
                j = mid - 1
            else:
                i = mid
        return self.top_candidate_at_time[i]
        """
    
    def calculate_top_candidate_at_time(self):
        top_candidate_at_time = list()
        prev_top_count = 0
        for i, cand in enumerate(self.persons):
            self.counter[cand] += 1
            if self.counter[cand] >= prev_top_count:
                top_candidate_at_time.append(cand)
                prev_top_count = self.counter[cand]
            else:
                top_candidate_at_time.append(top_candidate_at_time[-1])
        return top_candidate_at_time
        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)