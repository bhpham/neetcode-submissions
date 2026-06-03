class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #O(logm*n)
        # binary search
        rows, cols = len(matrix), len(matrix[0])
    
        for row in range(rows):
            # apply binary search
            l, r = 0, cols - 1
            while l <= r:
                m = (l + r) // 2
                print(matrix[row][m])
                if matrix[row][m] < target:
                    l = m + 1
                elif matrix[row][m] > target:
                    r = m - 1
                else:
                    return True
        
        return False