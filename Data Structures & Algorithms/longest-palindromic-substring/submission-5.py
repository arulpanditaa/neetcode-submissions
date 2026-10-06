class Solution:
    def longestPalindrome(self, s: str) -> str:

        best_srt, best_len = 0, 0 
        for i in range(len(s)):
                
                l, r = i, i+1
                if r < len(s) and s[l] == s[r] :
                    while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                        l, r = l-1, r+1
                    if ((r) - (l) + 1) > best_len:
                        best_len = ((r) - (l) + 1)
                        best_srt = l

                l, r = i, i            
                while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                    l, r = l-1, r+1
                if ((r) - (l) + 1) > best_len:
                    best_len = ((r) - (l) + 1)
                    best_srt = l
        
        return s[best_srt:best_srt+best_len]
                

        