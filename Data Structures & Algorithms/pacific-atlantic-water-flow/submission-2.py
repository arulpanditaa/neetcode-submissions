class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        flow_pa = set()
        flow_at = set()
        padq = deque()
        atdq = deque() 
        dc = [[1,0], [-1,0], [0,1], [0,-1]]

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i == 0 or j == 0:
                    padq.append((i, j))
                    flow_pa.add((i,j))
                if i == (len(heights) - 1) or j == (len(heights[i]) - 1):
                    atdq.append((i,j))
                    flow_at.add((i,j))
        def bfs(ocean, dq):
            while dq:
                i, j = dq.popleft()
                for r, c in dc:
                    row, col = i+r, j+c
                    if (row in range(len(heights))) and (col in range(len(heights[i]))) and heights[i][j] <= heights[row][col] and ((row, col) not in ocean):
                        ocean.add((row, col))
                        dq.append((row, col))
        
        bfs(flow_at, atdq)
        bfs(flow_pa, padq)
        
        ans = []
        for i, j in flow_at:
            if (i,j) in flow_pa:
                ans.append([i,j])
        return ans 



        


        