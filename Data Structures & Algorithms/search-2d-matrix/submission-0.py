class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1 2 4 8 10 11 12 13 14 20 30 40
        left = 0 
        right = (len(matrix) * len(matrix[0])) - 1
        
        while left <= right:
            mid = (left + right) // 2
            midX = mid // len(matrix[0])
            midY = mid % len(matrix[0])

            if target == matrix[midX][midY]:
                return True
            
            if target > matrix[midX][midY]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False