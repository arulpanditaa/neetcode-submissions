class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        answer = [0]* len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                diff = i - stack[-1][-1]
                answer[stack[-1][-1]] = diff
                stack.pop()
            stack.append([temp, i]) 
        return answer
            

        