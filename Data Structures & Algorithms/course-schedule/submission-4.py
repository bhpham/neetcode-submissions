class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            indegrees[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses


#TC: O(V + E) where V is number of courses and E is the number of prerequisities
#SC: O(V + E)