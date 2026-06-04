class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = top + (bottom-top) // 2 
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        left = 0
        right = (len(matrix[row]) - 1)
        
        while left <= right:
            column = left + (right - left) // 2 
            if matrix[row][column] > target:
                right = column - 1
            elif matrix[row][column] < target:
                left = column + 1
            else:
                return True 

        return False


        