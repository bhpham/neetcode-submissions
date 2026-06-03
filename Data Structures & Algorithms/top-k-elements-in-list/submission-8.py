class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        freqs = [[] for i in range(len(nums) + 1)]
        res = []

        for key, val in count.items():
            freqs[val].append(key)
        
        for i in range(len(freqs) - 1, -1, -1):
            for freq in freqs[i]:
                res.append(freq)
                k -= 1
                if k == 0:
                    return res