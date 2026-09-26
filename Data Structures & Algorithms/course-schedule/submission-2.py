class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, seen = [], set()
        for i in range(numCourses):
            graph.append([])
        for i, j in prerequisites:
            graph[j].append(i)

        def dfs(i):
            if i in seen:
                return False
            if graph[i] == []:
                return True
            seen.add(i)
            for j in range(len(graph[i])):
                if dfs(graph[i][j]) == False:
                    return False
            seen.remove(i)
            graph[i] = []
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
