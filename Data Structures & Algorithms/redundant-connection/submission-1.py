class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # degree = no of connections of a node 
        graph, degree, dq = [], [], deque()
        for i in range(len(edges)+1):
            graph.append([])
            degree.append(0) 
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1 
            degree[b] += 1
        for i in range(len(degree)):
            if degree[i] == 1:
                dq.append(i)
        while dq:
            node = dq.popleft()
            degree[node] -= 1
            for nb in graph[node]:
                degree[nb] -= 1
                if degree[nb] == 1:
                    dq.append(nb)
        for c, d in reversed(edges):
            if degree[c] == 2 and degree[d] == 2:
                return [c,d]
        return []
# Nodes that are in b/w the cycle don't even enter the for loop
                

        
        


        