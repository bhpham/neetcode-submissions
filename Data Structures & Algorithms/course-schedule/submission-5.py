class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            indegrees[pre] += 1
            adj[crs].append(pre)

        q = deque()
        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)

        visit = 0
        while q:
            node = q.popleft()
            visit += 1

            for nei in adj[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return visit == numCourses