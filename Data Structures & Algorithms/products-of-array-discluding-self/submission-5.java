class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = 1;
        }
        
        int prefix = 1;
        int posfix = 1;

        for (int i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }
        for (int j = n - 1; j >= 0; j--) {
            res[j] *= posfix;
            posfix *= nums[j];
        }
        return res;
    }
}  
