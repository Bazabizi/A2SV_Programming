class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = len(accounts)
        visited = defaultdict(int)
        count = {i:1 for i in range(size)}
        parent = {i :i for i in range(size)}
        
        def find(child):
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            return child     
        
        def union(x , y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if count[rep_x] > count[rep_y]:
                    parent[rep_x] = rep_y
                    count[rep_y] += count[rep_x]
                else:
                    parent[rep_y] = rep_x
                    count[rep_x] += count[rep_y]
        
        for idx , account in enumerate(accounts):
            for email in account[1:]:
                if email not in visited:
                    visited[email] = idx
                else:
                    union(find(visited[email]) , idx)
        
        ans = []
        temp = defaultdict(list)
        for idx in range(size):
            pidx = find(idx)
            temp[pidx].extend(accounts[idx][1:])
        
        for key , value in temp.items():
            account = []
            name = accounts[key][0]
            account.append(name)
            account.extend(sorted(list(set(value))))
            ans.append(account)
          

        return ans
                