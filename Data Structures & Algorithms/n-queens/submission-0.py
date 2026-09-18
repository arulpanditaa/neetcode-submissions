class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = []
        for i in range(n):
            board.append(["."]*n)
        res = []
        cols = set()
        diagL = set()
        diagR = set()

        def btrack(i):
            if i == n:
                sol = []
                for row in board:
                    sol.append("".join(row))
                res.append(sol)
                return None 
            for j in range(n):
                if j not in cols and i-j not in diagL and i+j not in diagR:
                    board[i][j] = "Q"
                    cols.add(j)
                    diagL.add(i-j)
                    diagR.add(i+j)
                    btrack(i+1)
                    board[i][j] = "."
                    cols.remove(j)
                    diagL.remove(i-j)
                    diagR.remove(i+j)
        btrack(0)
        return res 
            




        