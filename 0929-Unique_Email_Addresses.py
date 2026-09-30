import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            parts = email.split('@')
            parts[0] = re.sub('\.', '', parts[0])
            plusIdx = parts[0].find('+')
            if plusIdx >= 0:
                parts[0] = parts[0][:plusIdx]
            emailSet.add('@'.join(parts))
            
        return len(emailSet)

print(Solution().numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]))