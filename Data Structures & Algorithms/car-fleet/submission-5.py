class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        waqt = []
        stack = []
        
        for i, pos in enumerate(position):
            cars.append([pos, speed[i]])
        cars.sort()
        for i in range(len(cars)):
            dis = target - cars[i][0]
            time = dis / cars[i][1]
            waqt.append(time)

        for i in range(len(waqt) - 1, -1, -1):
            stack.append(waqt[i])
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  
        return len(stack)

                