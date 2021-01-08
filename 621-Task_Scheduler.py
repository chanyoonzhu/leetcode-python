"""
Clarification Questions
Q: Does case matter?
A: Only A-Z, upper case
"""

class Solution:
    """
    - Greedy with heap:
    - O(n-total), O(n-total) where total = 26, so is actually O(1), O(1)
    - Algorithm:
    1. count max possible idle time: most frequent letter (count - 1) * n # understanding this is crucial to solving the problem
    2. then calculating real idle time by removing idle time that is filled up with tasks
    3. adding real idle time to number of total tasks to get the final time needed
    """
    def leastInterval(self, tasks, n):
        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        task_counts.sort()

        task_max = task_counts.pop()
        idle_time = (task_max - 1) * n  # max possible idle time
        
        while task_counts and idle_time > 0:
            idle_time -= min(task_counts.pop(), task_max - 1) # min handles if current task is same size as task_max, it would only take task_max - 1 idle time

        idle_time = max(0, idle_time) # idle time cannot be less than zero

        return idle_time + len(task)

    
    """
    - Math: intuition see image: https://leetcode.com/problems/task-scheduler/solution/
    - O(n-total), O(n-total) where total = 26, so is actually O(1), O(1)
    - Algorithm:
    1. The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.
    2. Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.
    3. Find the maximum frequency: f_max = max(frequencies).
    4. Find the number of tasks which have the max frequency: n_max = frequencies.count(f_max).
    5. If the number of slots to use is defined by the most frequent task, it's equal to (f_max - 1) * (n + 1) + n_max.
    6. Otherwise, the number of slots to use is defined by the overall number of tasks: len(tasks).
    7. Return the maximum of these two: max(len(tasks), (f_max - 1) * (n + 1) + n_max).
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)

        
        