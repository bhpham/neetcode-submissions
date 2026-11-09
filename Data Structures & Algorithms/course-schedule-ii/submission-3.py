class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
            indegrees[dst] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)
        
        visit, output = 0, []
        while q:
            node = q.popleft()
            visit += 1
            output.append(node)

            for nei in adj[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return output[::-1] if visit == numCourses else []
