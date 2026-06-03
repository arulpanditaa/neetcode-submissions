class Solution:
    def isPalindrome(self, s: str) -> bool:

       combined = [char.lower() for char in s if char.isalnum()]
       left = 0
       right = (len(combined)- 1)

       while left<right:
        if combined[left] == combined[right]:
            left += 1
            right -= 1
        else:
            return False 
       return True 
        


        