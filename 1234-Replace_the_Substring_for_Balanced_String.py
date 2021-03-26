class Solution:

    """
    - sliding window
    - similar question: 76
    - algorithm: move right pointer to right until satisfies condition, then move left pointer to right to tighten window until condition not satisfied.
    """
    def balancedString(self, s: str) -> int:
        n = len(s)
        target_count = n // 4
        min_sublen = n
        counts = collections.Counter(s)
         
        left = 0
        for right in range(n):
            counts[s[right]] -= 1
            # left can be right + 1 when no char needs to be replaced
            while left < n and all(count <= target_count for count in counts.values()): # or use: all(n / 4 >= count[c] for c in 'QWER'):
                min_sublen = min(min_sublen, right - left + 1)
                counts[s[left]] += 1
                left += 1
                        
        return min_sublen