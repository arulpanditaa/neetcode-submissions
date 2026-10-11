class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        for j in range(len(text2)+1):
            dp.append(0)        
            
        for i in range(1, len(text1)+1):
            diag = 0 
            for j in range(1, len(text2)+1):
                prev_val = dp[j]
                if text1[i-1] == text2[j-1]:    
                    dp[j] = diag + 1
                else:    
                    dp[j] = max(dp[j], dp[j-1])
                diag = prev_val

        return dp[len(text2)]
