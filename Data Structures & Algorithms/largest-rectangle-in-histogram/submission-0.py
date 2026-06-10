class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
              index = stack.pop()
              
              if stack:
                left_wall = stack[-1]
              else:
                left_wall = -1
              width = i - left_wall - 1
              area = width * heights[index]
              max_area = max(area, max_area)
            stack.append(i)

        return max_area
        
    

            

              

        

