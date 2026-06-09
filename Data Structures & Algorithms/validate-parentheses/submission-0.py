class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        maps = {"}" : "{" , "]" : "[" , ")" : "(" }

        for bkt in s:
            if bkt in maps:
                if stack and maps[bkt] == stack[-1]:
                    stack.pop()
                else: 
                    return False 
            else:
                stack.append(bkt)
        return len(stack) == 0

        