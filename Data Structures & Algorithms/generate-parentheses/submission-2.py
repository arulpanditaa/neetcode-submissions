class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res, sol = [], []
        def btrack(a, b):
                if a == b == n:
                    res.append("".join(sol))
                    return None
                if a < n:
                    sol.append("(")
                    btrack(a + 1, b)
                    sol.pop()
                if b < a:
                    sol.append(")")
                    btrack(a, b + 1)
                    sol.pop()
        btrack(0, 0)
        return res
        
                
                


        