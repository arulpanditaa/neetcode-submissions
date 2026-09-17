class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        naksha = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res, sol = [], []

        def btrack(n):
            if len(sol) == len(digits):
                res.append("".join(sol))
                return None
            for j in range(0, len(naksha[int(digits[n])])):
                ans = naksha[int(digits[n])][j]
                sol.append(ans)
                btrack(n+1)
                sol.pop()
        
        if digits:
            btrack(0)
        return res