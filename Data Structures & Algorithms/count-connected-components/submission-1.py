class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph, ans = [], 0
        for i in range(n):
            graph.append([])
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dq, seen = deque(), set()
        for node in range(len(graph)):
            if node not in seen:
                dq.append(node)
                seen.add(node)
                ans += 1 
                while dq:
                    curr = dq.popleft()
                    for i in graph[curr]:
                        if i not in seen:
                            seen.add(i)
                            dq.append(i)
        return ans
                


        

        
