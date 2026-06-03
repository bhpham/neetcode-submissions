class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prefix = 1;
        int posfix = 1;
        int[] res = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        for (int j = nums.length - 1; j >= 0; j--) {
            res[j] *= posfix;
            posfix *= nums[j];
        }
        return res;
    }
}  
