class Solution:
    def numDecodings(self, s: str) -> int:

        if int(s[0]) == 0:
            prev = 0
        else:
            prev = 1
        prev_p = 1

        for i in range(1, len(s)):
            curr = 0 
            if int(s[i]) > 0:
                curr += prev
            if (10 <= int(s[i-1:i+1]) <= 26):
                curr += prev_p
            prev_p, prev = prev, curr 
        return prev 


        