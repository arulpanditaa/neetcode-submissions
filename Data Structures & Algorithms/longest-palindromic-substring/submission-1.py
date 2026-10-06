class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans_odd, ans_even = "", ""

        for i in range(len(s)):
                
                a, b = i, i+1
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a, b = a-1, b+1
                if len(s[a+1:b]) > len(ans_even):
                    ans_even = s[a+1:b]

                a, b = i, i            
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a, b = a-1, b+1
                if len(s[a+1:b]) > len(ans_odd):
                    ans_odd = s[a+1:b]
        
        if len(ans_odd) > len(ans_even):
            return ans_odd
        else:
            return ans_even
                

        