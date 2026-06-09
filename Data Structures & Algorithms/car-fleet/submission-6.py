class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        waqt = []
        stack = []
        
        for i, pos in enumerate(position):
            cars.append([pos, speed[i]])
        cars.sort(reverse = True)
        for i in range(len(cars)):
            dis = target - cars[i][0]
            time = dis / cars[i][1]
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  
        return len(stack)

                