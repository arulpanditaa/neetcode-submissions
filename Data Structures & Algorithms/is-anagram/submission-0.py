class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = [0]* 26

        if len(s) != len(t):
            return False 
        
        for i in range(len(s)):

            count[ord(s[i])- ord('a')] = count[ord(s[i])- ord('a')] + 1 

            count[ord(t[i])- ord('a')] = count[ord(t[i])- ord('a')] - 1 

        for value in count:
            if value != 0:
                return False 
        return True 






        
        