class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        int longest = 0;

        // Initialize the numSet
        for (int n : nums) {
            numSet.add(n);
        }    

        for (int n : nums) {
            if (!numSet.contains(n - 1)) {
                int nextNum = n + 1;
                while (numSet.contains(nextNum)) {
                    nextNum++;
                }
                longest = Math.max(longest, nextNum - n);
            }
        }
        return longest;
    }
}
