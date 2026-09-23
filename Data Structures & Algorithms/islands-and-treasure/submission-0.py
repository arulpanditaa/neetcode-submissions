class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        dq = deque()
        INF = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dq.append((i,j))
        while dq:
            i, j = dq.popleft()
            if i+1 < len(grid) and grid[i+1][j] == INF:
                grid[i+1][j] = grid[i][j] + 1
                dq.append((i+1,j))
            if i-1 >= 0 and grid[i-1][j] == INF:
                grid[i-1][j] = grid[i][j] + 1
                dq.append((i-1, j)) 
            if j+1 < len(grid[i]) and grid[i][j+1] == INF:
                grid[i][j+1] = grid [i][j] + 1
                dq.append((i, j+1))
            if j-1 >= 0 and grid[i][j-1] == INF:
                grid[i][j-1] = grid[i][j] + 1
                dq.append((i, j-1))


        
        
        