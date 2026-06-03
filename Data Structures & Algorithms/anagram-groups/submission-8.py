class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())

''' Dry running
res = {
    (1, 0 , 1 , 0, 0 , 1 , 0, 0): ["act", "cat"]
    (0, 0 ,0 , 1, 0 ,0 , 1, 1, 0, 0, 0 , 1): ["pots", "tops", "stop"]
    (1, 0, 0, 0, 1, 0, 1): ["hat"] 
}
--> [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
"act"
count = [1, 0 , 1 , 0, 0 , 1 , 0, 0]     # length of 26 characters
    Loop:
        c = 'a', count[26 - 26] += 1
        c = 'c', count[28 - 26] += 1
        c = 't', count[31 - 26] += 1
"cat"
count = [1, 0 , 1 , 0, 0 , 1 , 0, 0]  
    Loop:
        c = 'c', count[28 - 26] += 1
        c = 'a' , count[26 - 26] += 1
        c = 't', count[31 - 26] += 1
"pots"
count = [0, 0 ,0 , 1, 0 ,0 , 1, 1, 0, 0, 0 , 1]
    Loop:
        c = 'p', count[40 - 26] += 1
        c = 'o', count[39 - 26] += 1
        c = 't', count[31 - 26] += 1
        c = 's', count[45 - 26] += 1
'''