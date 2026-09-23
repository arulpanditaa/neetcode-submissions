class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        ans, fresh = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    dq.append((i, j))
        while fresh > 0 and dq:
            for a in range(len(dq)):
                i, j = dq.popleft()
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    fresh -= 1
                    grid[i+1][j] = 2
                    dq.append((i+1, j))
                if i-1 >= 0 and grid[i-1][j] == 1:
                    fresh -= 1
                    grid[i-1][j] = 2
                    dq.append((i-1, j))
                if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                    fresh -= 1
                    grid[i][j+1] = 2
                    dq.append((i, j+1))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    fresh -= 1
                    grid[i][j-1] = 2
                    dq.append((i, j-1))
            ans += 1
        if fresh == 0:
            return ans
        else:
            return -1 
        