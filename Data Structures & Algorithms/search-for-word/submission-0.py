class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ans = [False]
        def bt(a, b, idx_word):
            if idx_word == len(word) - 1:
                ans.append(True)
                return None 
            if (b + 1) < len(board[a]) and (idx_word + 1) < len(word) and word[idx_word + 1] == board[a][b+1]:
                letter = board[a][b+1]
                board[a][b+1] = "#"
                bt(a, b+1, idx_word + 1)
                board[a][b+1] = letter
            if (b - 1) >= 0 and (idx_word + 1) < len(word) and word[idx_word + 1] == board[a][b-1]:
                letter = board[a][b-1]
                board[a][b-1] = "#" 
                bt(a, b-1, idx_word + 1)
                board[a][b-1] = letter
            if (a + 1) < len(board) and (idx_word + 1) < len(word) and word[idx_word + 1] == board[a+1][b]:
                letter = board[a+1][b]
                board[a+1][b] = "#"
                bt(a+1, b, idx_word + 1)
                board[a+1][b] = letter
            if (a - 1) >= 0 and (idx_word + 1) < len(word) and word[idx_word + 1] == board[a-1][b]:
                letter = board[a-1][b]
                board[a-1][b] = "#"
                bt(a-1, b, idx_word + 1)
                board[a-1][b] = letter
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    letter = board[i][j]
                    board[i][j] = "#"
                    bt(i, j, 0)
                    board[i][j] = letter
        return ans[-1]


    
        
