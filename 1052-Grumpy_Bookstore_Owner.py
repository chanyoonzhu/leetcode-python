class Solution:
    """
    - accumulative sum - my solution
    - O(n + X), O(n)
    """
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        accumulated_sums = [0] * (n + 1)
        satisfaction_sums = [0] * (n + 1)
        for i, total in enumerate(customers):
            accumulated_sums[i + 1] = accumulated_sums[i] + total
            satisfaction_sums[i + 1] = satisfaction_sums[i]
            if not grumpy[i]:
                satisfaction_sums[i + 1] += total
            
        largest_satisfaction = float("-inf")
        for i in range(0, n + 1 - X):
            largest_satisfaction = max(largest_satisfaction, satisfaction_sums[i] + accumulated_sums[i + X] - accumulated_sums[i] + satisfaction_sums[n] - satisfaction_sums[i + X])
        
        return largest_satisfaction
    
    """
    - sliding window
    - O(n), O(n)
    """
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        already_satisfied = 0
        x_satisfaction_max = float("-inf")
        x_satisfaction = 0
        for i in range(n):
            if not grumpy[i]:
                already_satisfied += customers[i]
                customers[i] = 0 # don't forget reset to remove duplicates
            x_satisfaction += customers[i]
            if i - X >= 0:
                x_satisfaction -= customers[i - X]
            x_satisfaction_max = max(x_satisfaction_max, x_satisfaction)
        return already_satisfied + x_satisfaction_max