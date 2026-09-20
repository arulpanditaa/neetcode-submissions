class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
            else:
                return None

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans += 1 
                    dfs(i, j)
        return ans 
