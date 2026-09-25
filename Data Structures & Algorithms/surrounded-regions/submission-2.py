class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dq = deque()
        dc = [[1,0], [-1,0], [0,1], [0,-1]]
        no_change = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i == 0 or i ==  (len(board) - 1) or j == 0 or j == (len(board[i]) - 1)):
                    dq.append((i,j))
                    no_change.add((i,j))
        
        while dq:
            i, j = dq.popleft()
            for r, c in dc:
                row, col = i+r, j+c
                if row in range(len(board)) and col in range(len(board[row])) and board[row][col] == "O" and (row,col) not in no_change:
                    dq.append((row,col))
                    no_change.add((row,col))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i, j) not in no_change:
                    board[i][j] = "X"




            
        

        