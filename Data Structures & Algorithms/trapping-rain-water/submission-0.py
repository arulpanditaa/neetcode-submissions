class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = (len(height) - 1)
        area = 0
        left_max = height[left]
        right_max = height[right]
        while right > left:
            if right_max > left_max:
                left += 1 
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    area += left_max - height[left]
            else:
                right -= 1 
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    area += right_max - height[right]
        return area    
            
        



        
        