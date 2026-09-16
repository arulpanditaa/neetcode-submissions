class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res, sol = [], []

        def btrack(start):
            if start == len(s):
                res.append(sol[:])
                return None 
            for end in range(start, len(s)):
                ans = s[start:end + 1]
                if ans == ans[::-1]:
                    sol.append(ans)
                    btrack(end+1)
                    sol.pop()
                
        btrack(0)
        
        return res 


        