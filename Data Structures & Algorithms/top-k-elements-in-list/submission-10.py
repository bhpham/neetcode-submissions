class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqs = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freqs[c].append(n)
        for i in range(len(freqs) - 1, -1, -1):
            for freq in freqs[i]:
                res.append(freq)
                k -= 1
                if k == 0:
                    return res