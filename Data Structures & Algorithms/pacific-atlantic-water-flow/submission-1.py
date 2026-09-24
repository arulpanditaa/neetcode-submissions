class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        Pa = set()
        At = set()
        dq1 = deque()
        dq2 = deque() 
        dc = [[1,0], [-1,0], [0,1], [0,-1]]

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i == 0 or j == 0:
                    dq1.append((i, j))
                    Pa.add((i,j))
                if i == (len(heights) - 1) or j == (len(heights[i]) - 1):
                    dq2.append((i,j))
                    At.add((i,j))
        while dq1:
            i, j = dq1.popleft()
            for r, c in dc:
                row, col = i+r, j+c
                if (row in range(len(heights))) and (col in range(len(heights[i]))) and heights[i][j] <= heights[row][col] and ((row, col) not in Pa):
                    Pa.add((row, col))
                    dq1.append((row, col))
        while dq2:
            i, j = dq2.popleft()
            for r, c in dc:
                row, col = i+r, j+c
                if (row in range(len(heights))) and (col in range(len(heights[i]))) and heights[i][j] <= heights[row][col] and ((row,col) not in At):
                    At.add((row, col))
                    dq2.append((row, col))
        ans = []
        for i, j in At:
            if (i,j) in Pa:
                ans.append([i,j])
        return ans 



        


        