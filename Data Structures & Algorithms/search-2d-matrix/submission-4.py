class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0]) - 1, -1, -1):
                l, r = 0, col
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[row][mid] < target:
                        l = mid + 1
                    elif matrix[row][mid] > target:
                        r = mid - 1
                    else:
                        return True
        
        return False
                

    