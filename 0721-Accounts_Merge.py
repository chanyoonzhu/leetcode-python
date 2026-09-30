"""
- Set union (brutal force)
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mapping = defaultdict(list)
        
        for account in accounts:
            name, emails = account[0], set(account[1:])
            email_lists = []
            email_lists.append(emails)
            for other_emails in mapping[name]:
                if emails & other_emails:
                    email_lists[0] |= other_emails
                else:
                    email_lists.append(other_emails)
            mapping[name] = email_lists
        
        res = []
        for name in mapping:
            for emails in mapping[name]:
                res.append([name] + sorted(emails))
        return res

"""
- dfs
- O(NKlogNK): N - account n, K - max length of an account
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mapping = defaultdict(list) # email -> account no.
        visited_accounts = [False] * len(accounts)
        res = []
        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                mapping[email].append(i)
        
        def dfs(i):
            visited_accounts[i] = True
            emails = set()
            for email in accounts[i][1:]:
                emails.add(email)
                for nei_account in mapping[email]:
                    if not visited_accounts[nei_account]:
                        emails |= dfs(nei_account)
            return emails
                
        for i, account in enumerate(accounts):
            if not visited_accounts[i]:
                res.append([account[0]] + sorted(dfs(i)))
        return res

"""
- Union-find
- O(NKlogNK), O(NK)
"""
class UnionFind:
        def __init__(self, n):
            self.parents = [i for i in range(n)]
            self.sizes = [1] * n
            
        def find(self, x):
            if self.parents[x] != x:
                self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
        def union(self, x, y):
            parent_x, parent_y = self.find(x), self.find(y)
            if parent_x == parent_y: return
            if self.sizes[parent_x] >= self.sizes[parent_y]:
                self.parents[parent_y] = parent_x
                self.sizes[parent_x] += self.sizes[parent_y]
            else:
                self.parents[parent_x] = parent_y
                self.sizes[parent_y] += self.sizes[parent_x]

class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        id_to_name = {}
        id_to_email = {}
        
        id_ = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id: # easy to miss, dedup
                    email_to_id[email] = id_
                    id_to_name[id_] = name
                    id_to_email[id_] = email
                    id_ += 1
        
        uf = UnionFind(id_ + 1)
        for account in accounts:
            for i in range(2, len(account)):
                uf.union(email_to_id[account[1]], email_to_id[account[i]])
                
        id_to_connected_emails = defaultdict(set)
        for i in range(id_):
            id_to_connected_emails[uf.find(i)].add(id_to_email[i])
        
        res = []
        for (i, emails) in id_to_connected_emails.items():
            name = id_to_name[i]
            res.append([name] + sorted(emails))
        return res