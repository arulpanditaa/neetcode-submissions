class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != (n -1):
            return False
        graph = []
        for i in range(n):
            graph.append([])
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dq, seen = deque(), set()
        
        def bfs(srt_node):
            dq.append(srt_node)
            seen.add(srt_node)
            while dq:
                node = dq.popleft()
                for i in graph[node]:
                    if i not in seen:
                        dq.append(i)
                        seen.add(i)
        bfs(0)

        if len(seen) == n:
            return True
        else:
            return False









        