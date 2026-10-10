class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = []
        for i in range(m):
            row = []
            for i in range(n):
                row.append(-1)
            cache.append(row)

        def dfs(r,c):
            if r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if cache[r][c] != -1:
                return cache [r][c]
            cache[r][c] = (dfs(r+1, c) + dfs(r, c+1))
            return cache[r][c]

        return dfs(0,0)
 
        