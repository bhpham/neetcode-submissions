class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequents = [[] for _ in range(len(nums) + 1)]
        res = []
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, n in count.items():
            frequents[n].append(i)
        
        for j in range(len(frequents) - 1, -1, -1):
            for f in frequents[j]:
                res.append(f)
                k -= 1
                if k == 0:
                    return res[::-1]
                
        return []