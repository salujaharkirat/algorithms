class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            if direction == 0:
                for c in range(left, right + 1):
                    res.append(matrix[top][c])
                top += 1
                direction = 1
            elif direction == 1:
                for r in range(top, bottom + 1):
                    res.append(matrix[r][right])
                right -= 1
                direction = 2
            elif direction == 2:
                for c in range(right,left -1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
                direction = 3
            elif direction == 3:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
                direction = 0
        
        return res
        