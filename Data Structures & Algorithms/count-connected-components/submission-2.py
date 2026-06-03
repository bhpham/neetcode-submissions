class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Dfs
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
