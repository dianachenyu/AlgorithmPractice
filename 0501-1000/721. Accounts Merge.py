# Method 1: DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        names = dict()
        for account in accounts:
            name = account[0]
            emails = account[1: ]
            names[emails[0]] = name
            for i in range(1, len(emails)):
                graph[emails[0]].add(emails[i])
                graph[emails[i]].add(emails[0])
        
        def dfs(node, path):
            if node in path:
                return

            path.add(node)
            for nnode in graph[node]:
                if nnode not in path:
                    dfs(nnode, path)

        visited = set()
        res = []
        for email in names.keys():
            if email not in visited:
                path = set()
                dfs(email, path)
                visited |= path
                path = sorted(list(path))
                name = names[email]
                res.append([name] + path)
        return res



# Method 2: Union Find
class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            self.parent[max(pi, pj)] = min(pi, pj)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_idx = dict()
        for idx, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in email_idx:
                    uf.union(idx, email_idx[email])
                else:
                    email_idx[email] = idx
        
        idx_email = collections.defaultdict(list)
        for email, idx in email_idx.items():
            idx_email[uf.find(idx)].append(email)
        
        res = []
        for idx, emails in idx_email.items():
            res.append([accounts[idx][0]] + sorted(emails))
        return res



