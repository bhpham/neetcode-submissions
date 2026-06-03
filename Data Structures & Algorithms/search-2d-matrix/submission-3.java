class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        for (int row = 0; row < matrix.length; row++) {
            int l = 0, r = matrix[0].length - 1;
            while (l <= r) {
                int m = (l + r) / 2;
                if (matrix[row][m] < target) {
                    l++;
                } else if (matrix[row][m] > target) {
                    r--;
                } else {
                    return true;
                }
            }
        } 

        return false;   
    }
}
