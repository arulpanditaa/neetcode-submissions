class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bt(a, b, idx_word):
            if idx_word == len(word) - 1:
                return True
            if b+1 < len(board[a]) and word[idx_word + 1] == board[a][b + 1]:
                board[a][b + 1] = "#"
                if bt(a, b + 1, idx_word + 1):
                    board[a][b + 1] = word[idx_word + 1]
                    return True
                board[a][b + 1] = word[idx_word + 1]
            if b-1 >= 0 and word[idx_word + 1] == board[a][b - 1]:
                board[a][b - 1] = "#"
                if bt(a, b - 1, idx_word + 1):
                    board[a][b - 1] = word[idx_word + 1]
                    return True
                board[a][b - 1] = word[idx_word + 1]
            if a+1 < len(board) and word[idx_word + 1] == board[a + 1][b]:
                board[a + 1][b] = "#"
                if bt(a + 1, b, idx_word + 1):
                    board[a + 1][b] = word[idx_word + 1]
                    return True
                board[a + 1][b] = word[idx_word + 1]
            if a-1 >= 0 and word[idx_word + 1] == board[a - 1][b]:
                board[a - 1][b] = "#"
                if bt(a - 1, b, idx_word + 1):
                    board[a - 1][b] = word[idx_word + 1]
                    return True
                board[a - 1][b] = word[idx_word + 1]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    letter = board[i][j]
                    board[i][j] = "#"
                    if bt(i, j, 0):
                        board[i][j] = letter
                        return True
                    board[i][j] = letter
        return False
