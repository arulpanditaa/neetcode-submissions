class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(r, c, i):
            if i == len(word):
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and word[i] == board[r][c]:
                board[r][c] = "#"
                ans = ( bt(r, c + 1, i + 1) or bt(r, c - 1, i + 1) or bt(r + 1, c, i + 1) or bt(r - 1, c, i + 1) )
                board[r][c] = word[i]
                return ans 

        for r in range(len(board)):
            for c in range(len(board[r])):
                if word[0] == board[r][c]:
                    if bt(r, c, 0):
                        return True
        return False
