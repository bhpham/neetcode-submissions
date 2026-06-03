class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequents = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, n in count.items():
            frequents[n].append(i)
        
        for i in range(len(frequents) - 1, -1, -1):
            for freq in frequents[i]:
                res.append(freq)
                k -= 1
                if k == 0:
                    return res
        
        