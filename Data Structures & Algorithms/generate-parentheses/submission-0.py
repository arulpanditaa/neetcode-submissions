class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res, sol = [], []
        def btrack(a, b):
                if a == n and b == n:
                    res.append("".join(sol))
                    return None
                if a < n:
                    sol.append("(")
                    a += 1
                    btrack(a, b)
                    sol.pop()
                    a -= 1 
                if b < a:
                    sol.append(")")
                    b += 1
                    btrack(a, b)
                    sol.pop()
                    b -= 1
        btrack(0, 0)
        return res
        
                
                


        