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

        for i in range(len(waqt)):
            while stack and stack[-1] <= waqt[i]:
                stack.pop()

            stack.append(waqt[i])  
        return len(stack)

                