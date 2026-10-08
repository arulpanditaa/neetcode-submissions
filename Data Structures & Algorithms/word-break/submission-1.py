class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True 

        for i in range(1, len(dp)):
            for word in wordDict:
                l = len(word)
                if l <= i and dp[i-l] and s[i-l:i] == word:
                    dp[i] = True 
                    break 
        return dp[len(s)]
                 




                




        