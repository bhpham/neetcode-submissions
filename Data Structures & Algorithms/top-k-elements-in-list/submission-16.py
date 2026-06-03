'''
given integer array, and return k most frequent elements

Questions:
1/ Is k integer? Yes
2/ Can k be negative? no

input = [1,2,2,3,3,3] , k = 2
output = [2,3]

Approach: having a hashMap to store count of each integer
then track them to a 2D list of [value][key]  of hashmap
then scanning to the list, whenever we grab from list, decrement k until 0
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequents = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0) 
        
        for n, c in count.items():
            frequents[c].append(n)
        
        for i in range(len(frequents) - 1, -1, -1):
            for freq in frequents[i]:
                res.append(freq)
                k -= 1
                if k == 0:
                    return res

''' Dry runnning 
nums = [1,2,2,3,3,3] 
k = 2

count = {1:1, 2:2, 3:3}
frequents = [[], [1], [2], [3], [], [], []]
res = [3, 2]
k = 0

'''


