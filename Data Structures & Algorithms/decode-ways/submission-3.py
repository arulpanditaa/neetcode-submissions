class Solution:
    def numDecodings(self, s: str) -> int:

        
        prev, prev_p = 1, 1

        for i in range(len(s)):
            
            curr = 0
            if int(s[i]) > 0:
                curr += prev
            if i > 0 and (10 <= int(s[i-1:i+1]) <= 26):
                curr += prev_p
            prev_p, prev = prev, curr 
        return prev 


        