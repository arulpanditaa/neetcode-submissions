class Solution:
    def longestPalindrome(self, s: str) -> str:

        best_srt, best_len = 0, 0 
        for i in range(len(s)):
                
                l, r = i, i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l, r = l-1, r+1
                if ((r-1) - (l+1) + 1) > best_len:
                    best_len = ((r-1) - (l+1) + 1)
                    best_srt = l+1

                l, r = i, i            
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l, r = l-1, r+1
                if ((r-1) - (l+1) + 1) > best_len:
                    best_len = ((r-1) - (l+1) + 1)
                    best_srt = l+1
        
        return s[best_srt:best_srt+best_len]
                

        