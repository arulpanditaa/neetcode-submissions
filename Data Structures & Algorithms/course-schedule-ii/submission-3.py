class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph, no_of_pre = [], [0] * numCourses
        for i in range(numCourses):
            graph.append([])
        for course, pre in prerequisites:
            graph[pre].append(course)
            no_of_pre[course] += 1 
        
        dq, ans = deque(), []
        for course in range(len(no_of_pre)):
            if no_of_pre[course] == 0:
                dq.append(course)
        while dq:
            curr = dq.popleft()
            ans.append(curr)
            for nxt_course in graph[curr]:
                no_of_pre[nxt_course] -= 1
                if no_of_pre[nxt_course] == 0:
                    dq.append(nxt_course)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []

