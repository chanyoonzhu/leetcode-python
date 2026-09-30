"""
- similar: 358-Rearrange String k Distance Apart
"""
"""
Clarification Questions
Q: Does case matter?
A: Only A-Z, upper case
"""

"""
- priority queue
- O(nlogn, O(n))
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        idle_time = 0
        counts = [(-count, c) for c, count in Counter(tasks).items()]
        heapq.heapify(counts)
        
        while counts:
            is_last_round = True
            idle_time_cur_round = 0
            cooling = []
            for i in range(n + 1):
                if counts:
                    cooling.append((heapq.heappop(counts)))
                    if cooling[i][0] < -1: is_last_round = False
                else: 
                    idle_time_cur_round += 1
            
            if is_last_round: 
                break
            else:
                idle_time += idle_time_cur_round
             
            for count, c in cooling:
                if count < -1:
                    heapq.heappush(counts, (count + 1, c))
                    
        return len(tasks) + idle_time

    

"""
- greedy
- O(n) + O(26log26) = O(n), O(n)
- Algorithm:
1. The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.
2. Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.
3. Find the maximum frequency: f_max = max(frequencies).
4. Find the number of tasks which have the max frequency: n_max = frequencies.count(f_max).
5. If the number of slots to use is defined by the most frequent task, it's equal to (f_max - 1) * (n + 1) + n_max.
6. Otherwise, the number of slots to use is defined by the overall number of tasks: len(tasks) => when n is small
7. Return the maximum of these two: max(len(tasks), (f_max - 1) * (n + 1) + n_max).
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_count = max(counter.values())
        max_count_n = list(counter.values()).count(max_count)
        
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_n) # bucket number * bucket size (except last bucket) + last_bucket_size (see Problem 358),

        
        