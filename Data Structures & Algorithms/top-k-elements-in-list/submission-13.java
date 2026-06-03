class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] frequents = new List[nums.length + 1];

        for (int i = 0; i < frequents.length; i++) {
            frequents[i] = new ArrayList<>();
        }

        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int key = entry.getKey();
            int val = entry.getValue();
            frequents[val].add(key);
        }

        int[] res = new int[k];
        int idx = 0;
        for (int i = frequents.length - 1; i >= 0; i--) {
            for (int n : frequents[i]) {
                res[idx++] = n;
                if (idx == k) {
                    return res;
                }
            }
        }
        
        return res;

    }
}
