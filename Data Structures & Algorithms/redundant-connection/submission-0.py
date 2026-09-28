class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        graph = []
        for i in range(n+1):
            graph.append([])
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen, path, cycle = set(), [], set()
        def dfs(node, pita):
            seen.add(node)
            path.append(node)
            for nb in graph[node]:
                if nb == pita:
                    continue 
                if nb in seen:
                    idx = path.index(nb)
                    cycle.update(path[idx:])
                    return True #cycle found

                if dfs(nb, node) == True:
                    return True #cycle found
            path.pop()
            return False 
            #Cycle not found in this call
        dfs(1, -1)

        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]


        


                





        