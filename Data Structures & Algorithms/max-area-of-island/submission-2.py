class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def dfs(i,j):
            nonlocal curr
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
                grid[i][j] = 0
                curr += 1 
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
            else:
                return None 
            return curr
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    curr = 0
                    ans = max(ans, dfs(i,j))
        return ans 
        
        