class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                m = (l + r) //  2
                if matrix[i][m] < target:
                    l += 1
                elif matrix[i][m] > target:
                    r -= 1
                else:
                    return True
        
        return False