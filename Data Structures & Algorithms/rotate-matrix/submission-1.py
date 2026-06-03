class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r 
                topLeft = matrix[top][l + i]

                # move the bottomLeft to topLeft
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottomRight to bottomLeft
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move the topRight to bottomRight
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move the topLeft to topRight
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1
        

