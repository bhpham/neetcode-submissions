class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqs = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, n in count.items():
            freqs[n].append(i)
        
        for i in range(len(freqs) - 1, -1, -1):
            for freq in freqs[i]:
                res.append(freq)
                if len(res) == k:
                    return res
