class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while (top < bottom and left < right):
            # shift topLeft -> topRight
            for c in range(left, right):
                res.append(matrix[top][c])
            top += 1
            
            # shift topRight -> bottomRight
            for r in range(top, bottom):
                res.append(matrix[r][right - 1])
            right -= 1

            # checking inbound 
            if not (top < bottom and left < right):
                break

            # shift bottomRight -> bottomLeft
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][c])
            bottom -= 1

            # shift bottomLeft -> topLeft
            for r in range(bottom - 1, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
    
        return res