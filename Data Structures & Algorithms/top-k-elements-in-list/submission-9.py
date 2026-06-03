class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqs = [[] for i in range(len(nums) + 1)]
        res = []

        for i, n in count.items():
            freqs[n].append(i)
        
        for i in range(len(freqs) - 1, -1, -1):
            for freq in freqs[i]:
                res.append(freq)
                k -= 1
                if k == 0:
                    return res
                    