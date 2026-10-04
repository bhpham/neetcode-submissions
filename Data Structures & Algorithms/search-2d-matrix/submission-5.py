class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] < target:
                    l = mid + 1
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    return True
        
        return False

#TC: O(m * log(n)) where m is the number of rows and n is the number of cols
#SC: O(1) as we only used fixed variables

    