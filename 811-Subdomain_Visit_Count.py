"""
- hashmap
- O(n), O(n)
"""
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            counts[domain] += count
            for i in range(len(domain)):
                if domain[i] == ".":
                    counts[domain[i+1:]] += count
        return [f"{count} {domain}" for domain, count in counts.items()]