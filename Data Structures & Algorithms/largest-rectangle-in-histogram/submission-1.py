class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

      stack = []
      max_area = 0 
      
      for i in range(len(heights) + 1):
        if i == len(heights):
          height = 0
        else:
          height = heights[i] 
        while stack and heights[stack[-1]] > height:
          index = stack.pop()
          if stack:
            left_wall = stack[-1]
          else:
            left_wall = -1
          area = (i - left_wall - 1) * heights[index]
          max_area = max(area, max_area)
        stack.append(i)
      return max_area
        