class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen_row = [set() for row in range (9)] 
        seen_column = [set() for column in range (9)]
        seen_square = defaultdict(set)

        for row in range (9):

            for column in range(9):

                if board[row][column] == ".":
                    continue
                if board[row][column] in seen_row[row]:
                    return False
                seen_row[row].add(board[row][column])

                if board[row][column] in seen_column[column]:
                    return False
                seen_column[column].add(board[row][column])

                square_key = (row//3, column//3)
                if board[row][column] in seen_square[square_key]:
                    return False
                seen_square[square_key].add(board[row][column])
        return True

                