class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True 
        dictset = set(wordDict)

        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in dictset:
                    dp[i] = True 
                    break 
        return dp[len(s)]
                 




                




        