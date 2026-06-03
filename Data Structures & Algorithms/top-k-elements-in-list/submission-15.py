class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequents = [[] for _ in range(len(nums) + 1)]
        res = []
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, freq in count.items():
            frequents[freq].append(n)
        
        for i in range(len(frequents) - 1, -1, -1):
            for freq in frequents[i]:
                res.append(freq)
                k -= 1
                if k == 0:
                    return res