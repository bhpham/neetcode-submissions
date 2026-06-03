class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freqs = new List[nums.length + 1];

        for (int i = 0; i < freqs.length; i++) {
            freqs[i] = new ArrayList<>();
        }

        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freqs[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int idx = 0;
        for (int i = freqs.length - 1; i >= 0; i--) {
            for (int n : freqs[i]) {
                res[idx++] = n;
                if (idx == k) {
                    return res;
                }
            }
        }
        return res;
    }

}
