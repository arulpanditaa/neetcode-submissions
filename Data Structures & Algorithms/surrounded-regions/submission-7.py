class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dq = deque()
        dc = [[1,0], [-1,0], [0,1], [0,-1]]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i == 0 or i == (len(board) - 1) or j == 0 or j == (len(board[i]) - 1)):
                    dq.append((i,j))
        while dq:
            i, j = dq.popleft()
            board[i][j] = "T"
            for r, c in dc:
                row, col = i+r, j+c
                if row in range(len(board)) and col in range(len(board[row])) and board[row][col] == "O":
                    dq.append((row,col))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"



            
        

        