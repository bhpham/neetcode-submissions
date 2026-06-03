class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freqs = new List[nums.length + 1];

        for (int i = 0; i < freqs.length; i++) {
            freqs[i] = new ArrayList<>();
        }

        for (int n : nums) {
            count.put(n, 1 + count.getOrDefault(n, 0));
        }

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freqs[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = freqs.length - 1; i > 0 && index < k; i--) {
            for (int n : freqs[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }

        return res;

    }
}
